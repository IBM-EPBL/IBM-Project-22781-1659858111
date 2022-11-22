from flask import Flask, render_template, redirect, url_for, request
from .config import RAPID_API_KEY, API_URI
from . import auth
from . import news


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        app.config.from_pyfile(filename='config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/', methods=['POST', 'GET'])
    def index():

        if request.method == 'POST':
            q = request.form["search"]
            return redirect(url_for('news.news_fetch', query=q))
        else:
            return render_template('index.html', title = 'Home | News Tracker')

    app.register_blueprint(auth.bp)
    app.register_blueprint(news.bp)
    return app
