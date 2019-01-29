from flask_restplus import Api
from flask import Blueprint
from .main.resources import api as auth_ns
blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    version='1.0',
    title='Authentication',
    description='A simple Authentication API',
)

api.add_namespace(auth_ns)
