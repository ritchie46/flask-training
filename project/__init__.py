from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('../instance/flask.cfg')

from project.users.views import bp as users_bp
from project.classifier.views import bp as class_bp

app.register_blueprint(users_bp)
app.register_blueprint(class_bp)