#!/usr/bin/env python3
"""Force locale with URL parameter"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """
    This class contains a list of languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# configuring the app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Locale selector."""
    if request.args.get('locale') in app.config['LANGUAGES']
        return request.args.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    returns the rendered template `4-index.html`
    """
    locale = get_locale()

    return render_template('4-index.html', locale=locale)


if __name__ == '__main__':
    app.run(debug=True)
