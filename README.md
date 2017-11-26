# Real Estate Site

The Json file of the specified view is imported into the sqllite-database. The site of realtor agency allows you to filter real estate ads downloaded from the database.

### How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

### How to use
##### Sample run

```bash
# create DB from json file, sample json file in repo named ads.json
$ python3 db_create.py
# run server
$ python3 server.py -d
* Restarting with stat
* Debugger is active!
* Debugger PIN: 146-845-781
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now you can run localhost server on [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
Sample json file to create DB you can find in repo or download from [link](https://devman.org/media/filer_public/e5/62/e56287d2-9519-4e18-878a-6d4849b628e2/ads.json)

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
