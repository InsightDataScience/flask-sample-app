# Flask: Getting Started
This repo is to help you in setting up a simple Flask app. Use this to understand the elements of a Flask app.

### Installation
The installation steps are mentioned below. All these are based on this [page](https://flask.palletsprojects.com/en/1.1.x/installation/#create-an-environment).

* Clone this Github repo
  * `git clone https://github.com/InsightDataScience/flask-sample-app`

* Access repo folder. Create Python Virtual Environment
  * `cd flask-sample-app`
  * `python3 -m venv venv`

* Activate Environment
  * `. venv/bin/activate`

* Install flask
  * `pip install Flask`

### Quickstart: Hello World
In the dir `flask-sample-app`, there is a file `hello.py`. We'll use this to setup a hello-world Flask app.
* `export FLASK_APP=hello.py`
* `flask run --host=0.0.0.0`
* On a browser, type in `http://(your-EC2-public-IP):5000` in the location bar. You should see “Hello, World!” on your browser.
  * You may have to enable your EC2 Security-Group to have an inbound rule with `port:5000` and `source:anywhere`


### A simple FLASK_APP

Now that you have a hello-world Flask app working, we can build a slightly more involved app. This app involves a few components a webapp usually would have. We'll use the file `routes.py`, instead of `hello.py`.

* Stop the Flask hello-world app by issuing `ctrl-c`
* `export FLASK_APP=routes.py`
* `flask run --host=0.0.0.0`

Now you'll have a little more involved webapp. This should demonstrate on how to use CSS and JS files that's associated with a webapp.
