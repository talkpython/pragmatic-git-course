import random

import data
import flask
from flask import Flask

app = Flask(__name__)


@app.get('/')
def tell_a_joke():
    print('Beginning to tell a joke!')
    joke = random.choice(data.jokes)
    print(f'The joke we are telling is {joke}')
    return flask.render_template('joke.html', joke_text=joke)


if __name__ == '__main__':
    app.run(port=8001, debug=True)
