#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask
from models import storage
from models.state import State
from flask import render_template
from sqlalchemy.orm import scoped_session, sessionmaked


app = Flask(__name__)


@ app.teardown_appcontext
def teardown_db(exc):
    '''Call in this method storage.close()'''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_state():
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
