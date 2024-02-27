from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("main.html")

@app.route("/doggo")
def doggo():
    return render_template("doggos.html")
