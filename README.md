# Flask: getting started
This repo is to help you in setting up a simple Flask app. Use this to understand the elements of a Flask app.

## Installation
The installation steps are mentioned below. All these are based on this [page](https://flask.palletsprojects.com/en/1.1.x/installation/#create-an-environment).

1. Create Environment
* `mkdir myproject`
* `cd myproject`
* `python3 -m venv venv`

2. Activate Environment
* `. venv/bin/activate`

3. Install flask
* `pip install Flask`

## Quickstart
We will create a "hello-world" Flask app. Follow the steps:

* In the dir `myproject`, create a file `hello.py`. Content of `hello.py` should be:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

* `export FLASK_APP=hello.py`
* `flask run --host=0.0.0.0`
* On a browser, type in `http://(your-EC2-public-IP):5000` in the location bar. You should see “Hello, World!” on your browser.
  * You may have to enable your EC2 Security-Group to have an inbound rule with `port:5000` and `source:anywhere`
