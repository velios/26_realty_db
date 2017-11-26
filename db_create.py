from argparse import ArgumentParser
import json
import codecs

from server import db, Ads


def fetch_cmd_arguments():
    parser_description = 'Create sql-lite database from json file'
    parser = ArgumentParser(description=parser_description)
    parser.add_argument('-f', '--filepath',
                        help='Filepath to json sample',
                        default='ads.json')
    return parser.parse_args()


def load_data_from_articles_json(filepath='ads.json'):
    with codecs.open(filepath, "r", "utf_8_sig") as file_handler:
        return json.load(file_handler)


if __name__ == '__main__':
    cmd_args = fetch_cmd_arguments()
    source_json_filepath = cmd_args.filepath

    db.create_all()

    ads_json_list = load_data_from_articles_json(source_json_filepath)
    for ad in ads_json_list:
        db.session.add(Ads(**ad))
    db.session.commit()
