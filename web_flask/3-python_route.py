#!/usr/bin/python3
"""
Module: 1-hbnb_route.py

Write a script that starts a Flask web application

1st part:

- Import flask module
- save Flask class with "__name__" in a var
- Create a method named "whatever" with @.route decorator.
  - Inside .route will be ('/'). Use a route like (/python/<text>).
- Inside of the method return whatever the user request.
  - Ex. User request "/python/is_magic" will return "Python is magic".
    - Replace those underscore with spaces.
  - If not requested string then return "Python is cool"

2nd part:

- Implement if "__main__" = "__name__"; so it can call itself
- Enable the debugger so it can implement the configuration below.
- use run from Flask to configure host/port:
  - Configure to host 0.0.0.0
  - Configure the port which the app will listen to.
    - ex. port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def helloHBNB():
    """
    Return: Hello HBNB
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    """
    Return: HBNB
    """
    return 'HBNB'


@app.route('/c/<text>')
def cText(text):
    """
    Return: requested string
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/')
@app.route('/python')
def pythonDef():
    """
    Return: Python is cool
    """
    return "Python is cool"

# @app.route('/python', strict_slashes=False)

@app.route('/python/<text>')
def pythonText(text):
    """
    Return: requested string
    If theres not string in 'text' then return 'Python is cool'
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    """
    Configuring host/port
    """
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000, debug=True)
