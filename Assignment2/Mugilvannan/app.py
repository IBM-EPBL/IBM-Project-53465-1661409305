from flask import Flask;
from flask import render_template;
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/sign-in")
def sign_in():
    return render_template("sign-in.html")


@app.route("/sign-up")
def sign_up():
    return render_template("sign-up.html")