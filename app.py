from flask import Flask, render_template as rt

app = Flask(__name__)


@app.route("/")
def get_fizzbuzz():
    return rt("index.html")
