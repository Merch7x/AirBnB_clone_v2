#!/usr/bin/python3
"""Creates a basic python route"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", methods=["GET"], strict_slashes=False)
def list_states():
    """Returns a list of all states"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception=None):
    """Performs cleanup tasks by closing the db connection """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
