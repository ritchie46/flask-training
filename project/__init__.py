from flask import Flask

DEBUG = True

app = Flask(__name__)

import project.views