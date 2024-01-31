from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/collab-server/connect.html")
def connect():
    return render_template("connect.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
