#!/usr/bin/python3
"""
Module: 0-hello_route.py

Write a script that starts a Flask web application

1st part:

- Import flask module
- save Flask class with "__name__" in a var
- Create a method named "whatever" with @.route decorator.
  - Inside .route will be ('/'). You can use an entire route like ('/state')
- Inside of the method return "Hello HBNB"

2nd part:

- Implement if "__main__" = "__name__"; so it can call itself
- Enable the debugger so it can implement the configuration below.
- use run from Flask to configure host/port:
  - Configure to host 0.0.0.0
  - Configure the port which the app will listen to.
    - ex. port 5000
"""

from flask import Flask, request
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states_list')
def statesList():
    """
    Display a list of states in a specific order
    """
    return render_templates('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """
    Close a connection after a request in the app
    """
    storage.close()


if __name__ == "__main__":
    """
    Configuring host/port
    """
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000, debug=True)
