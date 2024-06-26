#!/usr/bin/python3
"""Starts a minimal python app
Creates routes for the app
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello():
    """Prints out hello to the root route of the flask app"""
    greeting = "Hello HBNB!"
    return greeting


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
