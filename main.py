#!/usr/bin/env python
import logging
import random
from flask import Flask, render_template
from flask_ask import Ask, statement, question

# import sys
# sys.path.insert(0, './lib/')
from lib.dir import Directions
from lib.config import ORIGIN, ORIGIN_NAME

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

m2mi = 0.000621371

ALREADY_THERE_MESSAGES = [
        "You're kind of already there.",
        "Is this a joke? Where already there",
        "Are you blind? This is " + ORIGIN_NAME,
        "Take two steps forward. Voila. You have arrived.",
        "Look up fool. You have arrived.",
        "Turn right. Turn right. You have arrived",
        "Turn 180 degrees. Turn another 180 degrees. You have arrived."
        ]

def getAlreadyThereResponse():
    return random.choice(ALREADY_THERE_MESSAGES)

@ask.launch

def new_session():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)

@ask.intent("QueryIntent")

def get_route(destination):
    print '='*88

    region = ", las vegas"

    directions = Directions(ORIGIN, destination + region)
    print directions
    print directions.directions_result

    instructions = directions.instructions

    # Remove excess instruction: "Walk to [region]"
    # instructions = instructions[:len(instructions) - 1]

    print ". ".join(instructions)

    directions_msg = render_template('route', directions = ". ".join(instructions), distance=directions.distance['text'], duration=directions.duration['text'])
    return statement(directions_msg)

if __name__ == '__main__':
    app.run(debug=True)
