#!/usr/bin/env python3
"""Implement Basic Babel setup."""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Implement Basic Babel setup."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """Implement Basic Babel setup."""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
