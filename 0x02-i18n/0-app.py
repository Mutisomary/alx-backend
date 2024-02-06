#!/usr/bin/env python3

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """the home page function"""
    title = 'Welcome to Holberton'
    text = 'Hello world'
    return render_template('index.html', title=title, text=text)


if __name__ == '__main__':
    app.run(debug=True)
