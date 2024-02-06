#!/usr/bin/env python3
"""simple flask application"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """config file"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Using the Config class as the configuration for the Flask app
app.config.from_object(Config)


@app.route('/')
def hello_world():
    """the home page function"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
