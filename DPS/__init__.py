import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'dps.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return render_template('index.html', Title="Tytuł")

    @app.route('/')
    def homepage():
        return render_template('homepage.html', Title="Powitanie")

    @app.route('/sygnal')
    def signal():
        return render_template('basic.html', Title="Sygnał ")

    @app.route('/sygnaly-podstawowe')
    def basic():
        return render_template('signal.html', Title="Podstawowe sygnały jednowymiarowe")
    return app
