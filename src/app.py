import os

from flask import Flask

from .extensions import db, migrate
from .apps.samples.views import blueprint as sample_bp


def create_app(env='dev'):
    app = Flask(__name__, template_folder='./templates')

    settings = os.path.abspath('./settings/{}.py'.format(env))
    app.config.from_pyfile(settings)

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app):
    app.register_blueprint(sample_bp, url_prefix='/api/samples')


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
