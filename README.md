# Flask: Getting Started
This repo is to help you in setting up a simple Flask app. Use this to understand the elements of a Flask app. This document contains of the following sections:
1. [Installation](#installation)
2. [Quickstart](#quickstart-hello-world)
3. [Simple FLASK_APP](#a-simple-flask_app)
4. [Simple FLASK_APP on port 80](#a-simple-flask_app-port-80)
5. [Intro to Web: Client-Server](#intro-to-web-client-server-model)

### Installation
It's recommended to do this on a new EC2 instance. So do spin up a new one if you don't have one yet.

The installation steps are mentioned below. All these are based on this [page](https://flask.palletsprojects.com/en/1.1.x/installation/#create-an-environment).

* Clone this Github repo
  * `git clone https://github.com/InsightDataScience/flask-sample-app`

* Access repo folder. Create Python Virtual Environment
  * `cd flask-sample-app`
  * `python3 -m venv venv`
    * If you are seeing an error, you may have to run `python3 -m venv venv --without-pip`

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

Reload your web browser with the same link you used before. You should see a page with a couple of links and buttons on it. This should demonstrate on how to use CSS and JS files that's associated with a webapp.

### A simple FLASK_APP (port 80)
Now we will run Flask app on port 80 - the default HTTP port for any webpage request.

**WARNING: This method should NOT be used in any other production environment. This is only a quick way to have your Flask app running on port 80 for Insight Project**

* Switch to user `su`
  * `sudo su - `

* Go to previous folder
  * `cd /home/ubuntu/repo/flask-sample-app`

* `python3 -m venv venv`
  * If you are seeing an error, you may have to run `python3 -m venv venv --without-pip`

* Activate Environment
  * `. venv/bin/activate`

* Install flask. Previous install was done for user `ubuntu`. Now we'll have to do same for user `su`.
  * `pip install Flask`

* `export FLASK_APP=routes_port80.py`

* Run Flask app in background. This should
  * `nohup flask run --host=0.0.0.0 --port=80 &`

### Intro to Web: client-server model

Once you have this app working, take time to understand how a webapp works. Here's a good [intro](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works) on how web works. Essentially there are 2 parts:
* **client-code**: Everything that's related to a webpage that appears in a web browser. In this case, client-code roughly includes everything in folders `static`, and `templates`.
* **server-code**: Flask server that "serves" webpages. In this case, both files `hello.py`, `routes.py`, and `routes_port80.py` are server-code.

`client` makes requests that are served by routes in server-code.

Type some text in the textarea you see in the page. Click button 'Use Route'. You should see text printed on browser's [console](https://developers.google.com/web/tools/chrome-devtools/console).

The following happened when you clicked button 'Use Route':
* (client) In JavaScript file `windowScript`, user-input is stored in variable `userName`. This value is sent to server.
* (server) In file `routes_port80`, user-input is received in variable `username` (line 17).
* (server) The same `username)` is returned with "User" prefixed.
* (client) Back in JavaScript file `windowScript`, the new string is received in variable `data`. This is printed on the console.

The above steps demonstrates a very simple example of how data is sent between client and server. This should give you an idea of a simple webapp now.
