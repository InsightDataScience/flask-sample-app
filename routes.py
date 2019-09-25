from flask import Flask, escape, render_template
app = Flask(__name__)

# Root path that returns home.html
@app.route('/')
def home():
    return render_template("home.html")

# About page
@app.route('/about')
def about():
    return render_template("about.html")

# Route that accepts a username(string) and returns it. You can use something similar
#   to fetch details of a username
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/userwithslash/<username>/')
def show_user_profile_withslash(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
