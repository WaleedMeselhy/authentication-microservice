import os

from flask import Flask
from flask_cors import CORS


def create_app(config_name):
    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    print('app_settings', config_name)
    app.config.from_object(config_name)
    app.config['JWT_PRIVATE_KEY'] = app.config['JWT_PRIVATE_KEY'].replace(
        '\\n', '\n')
    app.config['JWT_PUBLIC_KEY'] = app.config['JWT_PUBLIC_KEY'].replace(
        '\\n', '\n')
    from .jwt_controller import jwt
    jwt.init_app(app)
    return app
