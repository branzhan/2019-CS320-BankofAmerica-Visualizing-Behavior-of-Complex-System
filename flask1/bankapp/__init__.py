import os

from flask import Flask, send_from_directory, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS, cross_origin

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'bankapp.sqlite'),
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
        return 'Hello, World! from flask1'

    @app.route('/')
    def homepage():
        return render_template("homepage.html")

    # entry points for original code
    @app.route("/originals/")
    def original_index():
        return redirect( url_for("originals",filename="dashboard.html"))

    @app.route("/originals/index.html")
    def original_index1():
        return redirect(url_for("originals",filename="dashboard.html"))

    # 
    @app.route('/originals/<path:filename>')
    def originals(filename):
        return send_from_directory( app.root_path+ "/originals/", filename)

#        return send_from_directory( url_for("originals",filename) )


    # entry points for D3 live graphics

    from . import titanic
    titanic.init_db( app )
    app.register_blueprint(titanic.bp)


    # set up simple data base app from flask tutorial example
    from . import db
    db.init_app(app)

#    from . import auth
#    app.register_blueprint(auth.bp)

#    from . import blog
#    app.register_blueprint(blog.bp)
#    app.add_url_rule('/', endpoint='index')

    return app
    