from argparse import ArgumentParser
from os.path import abspath, dirname

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_filters import apply_filters


basedir = abspath(dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{basedir}/ads.db'.format(basedir=basedir)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Ads(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    settlement = db.Column(db.String(64), index = True)
    under_construction = db.Column(db.Boolean)
    description = db.Column(db.String(300))
    price = db.Column(db.Integer)
    oblast_district = db.Column(db.String(64))
    living_area = db.Column(db.Integer)
    has_balcony = db.Column(db.Boolean)
    address = db.Column(db.String(120))
    construction_year = db.Column(db.Integer)
    rooms_number = db.Column(db.Integer)
    premise_area = db.Column(db.Float)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<User {}>'.format(self.settlement)


def fetch_cmd_arguments():
    parser_description = 'Run flask server'
    parser = ArgumentParser(description=parser_description)
    parser.add_argument('-d', '--debug_mode',
                        help='Run in debug mode',
                        action='store_true')
    return parser.parse_args()


@app.route('/')
def ads_list():
    page = request.args.get('page', 1)
    oblast_district = request.args.get('oblast_district')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    new_building = request.args.get('new_building')

    filters = [{'field': 'active', 'value': True}]
    if new_building:
        filters.append({
            'or': [
                {'field': 'construction_year', 'op': 'is_null'},
                {'field': 'construction_year', 'op': '>=', 'value': 2016}
            ]
        })
    if oblast_district:
        filters.append({'field': 'oblast_district', 'value': oblast_district})
    if min_price:
        filters.append({'field': 'price', 'op': '>=', 'value': min_price})
    if max_price:
        filters.append({'field': 'price', 'op': '<=', 'value': max_price})

    filtered_query = apply_filters(Ads.query, filters)

    POSTS_PER_PAGE = 15
    ads = (filtered_query
           .paginate(int(page), POSTS_PER_PAGE, False))
    return render_template('ads_list.html', ads=ads)


if __name__ == "__main__":
    cmd_args = fetch_cmd_arguments()
    if cmd_args.debug_mode:
        app.config['DEBUG'] = True
    app.run()
