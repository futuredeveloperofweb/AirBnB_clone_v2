#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask
from models import storage
from flask import render_template
from models import *
from sqlalchemy.orm import scoped_session, sessionmaked


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state():
    '''display a HTML page: (inside the tag BODY)'''
    states = sorted(storage.all(State).values()),
                    key = lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@ app.teardown_appcontext
def teardown_db(exc):
    '''Call in this method storage.close()'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
