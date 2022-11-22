from flask import Flask, render_template
from . import config
from . import auth


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        app.config.from_pyfile(filename='config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return render_template('index.html', title = 'Home | News Tracker')

    app.register_blueprint(auth.bp)
    return app
