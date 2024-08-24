#!/usr/bin/python3
"""This script starts a Flask web application"""


# import Flask class from flask module
from flask import Flask

# create an instance called app of the class by passong the __name__ variable
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/airbnb-onepage/')
def index():
    """display "Hello HBNB!"

    Returns:
        str: text on the index page
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
