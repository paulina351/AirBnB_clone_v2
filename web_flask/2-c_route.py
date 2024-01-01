#!/usr/bin/python3
"""A  script that starts a Flask web application
   /c/<text>: display “C ” followed by the value of
   the text variable (replace underscore _ symbols
   with a space )
"""


from flask import Flask
from markupsafe import escape
import re

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route("/c/is_fun", strict_slashes=False)
def c_route():
    return "C is fun"


@app.route("/c/cool", strict_slashes=False)
def c_route_2(cool):
    return "C cool"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
