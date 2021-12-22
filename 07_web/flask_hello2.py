from flask import Flask, render_template
from flask.templating import render_template_string

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hello.html",
    title="Hello")

@app.route("/first")
def first_page():
    return render_template(
        "first.html",
        title="First Page")

@app.route("/second")
def Second_page():
    return render_template("second.html",
    title="Second Page")

if __name__ == "__main__":
    app.run(host="0.0.0.0")