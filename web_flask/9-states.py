#!/usr/bin/python3
""" Starts a Flask web application. """
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False, defaults={'id': None})
@app.route('/states/<id>', strict_slashes=False)
def states_list(id):
    return render_template('9-states.html', states=storage.all("State"),
                           id=id)


@app.teardown_appcontext
def teardown_app(Error):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_states():
    return render_template('8-cities_by_states.html',
                           states=storage.all("State"))


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
