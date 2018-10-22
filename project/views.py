from project import app
from flask import render_template
import random


@app.route('/')
def index():

    enthusiasm = int(random.uniform(2, 8))

    return render_template('index.html', enthusiasm=enthusiasm)