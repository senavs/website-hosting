from flask import Flask

from .configuration import CONFIG
from .backend.main import app_main
from .backend.tipo_pagamento import app_tipo_pagamento
from .backend.tipo_quarto import app_tipo_quarto


def create_app(config_name: str = 'develop'):
    # configurations
    app = Flask(__name__,
                static_folder='frontend/static',
                template_folder='frontend/templates')
    app.config.from_object(CONFIG[config_name])

    # init app

    # blueprints
    app.register_blueprint(app_main)
    app.register_blueprint(app_tipo_pagamento)
    app.register_blueprint(app_tipo_quarto)

    return app
