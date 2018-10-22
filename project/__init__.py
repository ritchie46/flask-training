from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('../instance/flask.cfg')

import project.views