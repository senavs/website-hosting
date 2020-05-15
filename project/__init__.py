from flask import Flask

from .configuration import CONFIG
from .backend.main import app_main
from .backend.quarto import app_quarto


def create_app(config_name: str = 'develop'):
    # configurations
    app = Flask(__name__)
    app.config.from_object(CONFIG[config_name])

    # init app

    # blueprints
    app.register_blueprint(app_main)
    app.register_blueprint(app_quarto)

    return app
