#!/usr/bin/python3
'''script that starts a Flask web application:'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''display “Hello HBNB!”'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''display “HBNB”'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    '''display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )'''
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def text2(text):
    '''display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )'''
    if text is None:
        return 'Python is cool'
    else:
        return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
