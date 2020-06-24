import os

from flask import Flask, render_template, request, flash, redirect, url_for
from .graphsgenerated import kronecker_graphs, step_graphs, rectangle_graphs, triangle_graphs, exp_graphs, \
    sinusoidal_graphs, aliasing_graphs
from .question import question_section1, question_section2, question_section3


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
        return render_template('homepage.html', Title="Strona główna")

    @app.route('/sygnal')
    def signal():
        return render_template('basic.html', Title="Sygnał ", link2 = 'sygnaly-zespolone')

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
                               sinusoidal_c=sinusoidal_graphs_c, sinusoidal_d=sinusoidal_graphs_d,
                               link1='sygnaly-zespolone' , link2='parametry-sygnalow'
                               )

    @app.route('/sygnaly-zespolone')
    def complexsignal():
        return render_template('complexsignal.html', Title="Sygnały zespolone", link1='sygnal' , link2='sygnaly-podstawowe')

    @app.route('/parametry-sygnalow')
    def signalparametric():
        return render_template('signalparameters.html', Title="Parametry sygnału", link1='sygnaly-podstawowe',
                               link2='probkowanie-aliasing')

    @app.route('/probkowanie-aliasing')
    def sampled():
        aliasing_svg = aliasing_graphs()
        return render_template('sampled.html', Title="Próbkowanie i aliasing", aliasing_svg=aliasing_svg,
                               link1='parametry-sygnalow', link2='sygnal-zadania')

    @app.route('/sygnal-zadania')
    def signalTasks():
        return render_template('signaltasks.html', Title="Sygnały - zadania w Pythonie",
                               link1='parametry-sygnalow', link2='sygnal-quiz')

    @app.route('/sygnal-quiz', methods=['GET', 'POST'])
    def signalquiz():
        if request.method == 'POST':
            points = 0
            reply = request.form
            for pnr, reply_u in reply.items():
                if reply_u == question_section1[int(pnr)]['true_answer']:
                    points += 1
            flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(points))
            return redirect(url_for('signalquiz'))

        return render_template('quiz.html', Title="Sygnały - quiz", questions=question_section1,
                               link1='sygnal-zadania', link2='szereg-fouriera')

    @app.route('/szereg-fouriera')
    def fourier():
        return render_template('fourier.html', Title="Rozwinięcie sygnału w szereg Fouriera", link2='cft')

    @app.route('/cft')
    def cft():
        return render_template('cft.html', Title="Całkowe przekształcenie Fouriera", link1='szereg-fouriera',
                               link2='dft')

    @app.route('/dft')
    def dft():
        return render_template('dft.html', Title="Dyskretne przekształcenie Fouriera", link1='cft', link2='widmo')

    @app.route('/widmo')
    def spectrum():
        return render_template('spectrum.html', Title="Widmo sygnału", link1='dft', link2='analiza-czestotliwosciowa-zadania')

    @app.route('/analiza-czestotliwosciowa-zadania')
    def spectrumtasks():
        return render_template('spectrumtasks.html', Title="Analiza częstotliwościowa - zadania w Pythonie",
                               link1='widmo', link2='analiza-czestotliwosciowa-quiz')

    @app.route('/analiza-czestotliwosciowa-quiz', methods=['GET', 'POST'])
    def spectrumquiz():
        if request.method == 'POST':
            points = 0
            reply = request.form
            for pnr, reply_u in reply.items():
                if reply_u == question_section2[int(pnr)]['true_answer']:
                    points += 1
            flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(points))
            return redirect(url_for('spectrumquiz'))

        return render_template('quiz.html', Title="Analiza częstotliwościowa - quiz", questions=question_section2,
                               link1='analiza-czestotliwosciowa-zadania', link2='przeksztalcenie-z')

    @app.route('/przeksztalcenie-z')
    def ztransform():
        return render_template('ztransform.html', Title="Transformata Z", link2='filtry-cyfrowe')

    @app.route('/filtry-cyfrowe')
    def digitalfilter():
        return render_template('digitalfilter.html', Title="Filtry cyfrowe", link1='przeksztalcenie-z', link2='fir')

    @app.route('/fir')
    def fir():
        return render_template('fir.html', Title="Filtr o skończonej odpowiedzi impulsowej",
                               link1='filtry-cyfrowe', link2='iir')

    @app.route('/iir')
    def iir():
        return render_template('iir.html', Title="Filtr o nieskończonej odpowiedzi impulsowej",
                               link1='fir', link2='filtry-zadania')

    @app.route('/filtry-zadania')
    def filtertask():
        return render_template('filtertask.html', Title="Filtry cyfrowe - zadania w Pythonie",
                               link1='iir', link2='filtry-quiz')

    @app.route('/filtry-quiz', methods=['GET', 'POST'])
    def filterquiz():
        if request.method == 'POST':
            points = 0
            reply = request.form
            for pnr, reply_u in reply.items():
                if reply_u == question_section3[int(pnr)]['true_answer']:
                    points += 1
            flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(points))
            return redirect(url_for('filterquiz'))

        return render_template('quiz.html', Title="Filtry cyfrowe - quiz", questions=question_section3,
                               link1='filtry-zadania', link2='qrs')

    @app.route('/qrs')
    def qrs():
        return render_template('qrs.html', Title="Detekcja zespołu QRS", link2='qrs-python')

    @app.route('/qrs-python')
    def qrstask():
        return render_template('qrstask.html', Title="Detekcja zespołu QRS - zadanie w Pythonie", link1='qrs')

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html')
    return app

