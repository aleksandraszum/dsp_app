import os

from flask import Flask, render_template
from .graphsgenerated import kronecker_graphs, step_graphs, rectangle_graphs, triangle_graphs, exp_graphs, \
    sinusoidal_graphs, aliasing_graphs


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
    @app.route('/')
    def homepage():
        return render_template('homepage.html', Title="Powitanie")

    @app.route('/sygnal')
    def signal():
        return render_template('basic.html', Title="Sygnał ")

    @app.route('/sygnaly-podstawowe')
    def basic():
        kronecker_graphs_c, kronecker_graphs_d = kronecker_graphs()
        step_graphs_c, step_graphs_d = step_graphs()
        rectangle_graphs_c, rectangle_graphs_d = rectangle_graphs()
        triangle_graphs_c, triangle_graphs_d = triangle_graphs()
        exp_graphs_c, exp_graphs_d = exp_graphs()
        sinusoidal_graphs_c, sinusoidal_graphs_d = sinusoidal_graphs()

        return render_template('signal.html', Title="Podstawowe sygnały jednowymiarowe", kronecker_c=kronecker_graphs_c,
                               kronecker_d=kronecker_graphs_d, step_c=step_graphs_c,
                               step_d=step_graphs_d, rectangle_c=rectangle_graphs_c, rectangle_d=rectangle_graphs_d,
                               triangle_c=triangle_graphs_c, triangle_d=triangle_graphs_d,
                               exp_c=exp_graphs_c, exp_d=exp_graphs_d,
                               sinusoidal_c=sinusoidal_graphs_c, sinusoidal_d=sinusoidal_graphs_d
                               )

    @app.route('/sygnaly-zespolone')
    def complexsignal():
        return render_template('complexsignal.html', Title="Sygnały zespolone")

    @app.route('/parametry-sygnalow')
    def signalparametric():
        return render_template('signalparameters.html', Title="Parametry sygnału")

    @app.route('/probkowanie-aliasing')
    def sampled():
        aliasing_svg = aliasing_graphs()
        return render_template('sampled.html', Title="Próbkowanie i aliasing", aliasing_svg=aliasing_svg)

    @app.route('/sygnal-zadania')
    def signalTasks():
        return render_template('signaltasks.html', Title="Sygnały - zadania w Pythonie")

    @app.route('/sygnal-quiz')
    def signalquiz():
        return render_template('signalquiz.html', Title="Sygnały - quiz")

    @app.route('/szereg-fouriera')
    def fourier():
        return render_template('fourier.html', Title="Rozwinięcie sygnału w szereg Fouriera")

    @app.route('/cft')
    def cft():
        return render_template('cft.html', Title="Całkowe przekształcenie Fouriera")

    @app.route('/dft')
    def dft():
        return render_template('dft.html', Title="Dyskretne przekształcenie Fouriera")

    @app.route('/widmo')
    def spectrum():
        return render_template('spectrum.html', Title="Widmo sygnału")

    @app.route('/analiza-czestotliwosciowa-zadania')
    def spectrumtasks():
        return render_template('spectrumtasks.html', Title="Analiza częstotliwościowa - zadania w Pythonie")

    @app.route('/analiza-czestotliwosciowa-quiz')
    def spectrumquiz():
        return render_template('spectrumquiz.html', Title="Analiza częstotliwościowa - quiz")

    @app.route('/przeksztalcenie-z')
    def ztransform():
        return render_template('ztransform.html', Title="Transformata Z")

    @app.route('/filtry-cyfrowe')
    def digitalfilter():
        return render_template('digitalfilter.html', Title="Filtry cyfrowe")

    @app.route('/fir')
    def fir():
        return render_template('fir.html', Title="Filtr o skończonej odpowiedzi impulsowej")

    @app.route('/iir')
    def iir():
        return render_template('iir.html', Title="Filtr o nieskończonej odpowiedzi impulsowej")

    @app.route('/filtry-zadania')
    def filtertask():
        return render_template('filtertask.html', Title="Filtry cyfrowe - zadania w Pythonie")

    @app.route('/iir')
    def filterquiz():
        return render_template('filterquiz.html', Title="Filtry cyfrowe - quiz")
    return app

# C:\Users\X\PycharmProjects\DSP_webapp\DPS\templates
