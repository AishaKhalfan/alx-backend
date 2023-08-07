#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    This class contains a list of languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# configuring the app
app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """
    returns the rendered template `index.html`
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
