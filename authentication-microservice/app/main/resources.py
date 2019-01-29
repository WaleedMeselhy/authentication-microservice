from flask_restplus import (Namespace, fields, Resource)
from .jwt_controller import check_login
# @api.errorhandler(exceptions.InvalidHeaderError)
# def invalid_token_callback(error):
#     # we have to keep the argument here,
#     # since it's passed in by the caller internally
#     return {
#         'message': 'Signature verification failed.',
#         'error': 'invalid_token'
#     }, 401
#
#
# @api.errorhandler(exceptions.NoAuthorizationError)
# def missing_token_callback(error):
#     return {
#         "description": "Request does not contain an access token.",
#         'error': 'authorization_required',
#         'message': 'ssssssss'
#     }, 401

api = Namespace('auth', description='AUTH operations')
user = api.model(
    'User', {
        'username': fields.String(required=True, description='username'),
        'password': fields.String(required=True, description='password')
    })

success_authenticate = api.model(
    'Success_Authenticate', {
        'access_token': fields.String(
            required=True, description='access_token'),
        'refresh_token': fields.String(
            required=True, description='refresh_token')
    })

error = api.model(
    'error', {
        'code':
        fields.Integer(required=True, description='code of error'),
        'message':
        fields.String(required=True, description='message of error'),
        'message_type':
        fields.String(required=True, description='message_type of error'),
        'gui_type':
        fields.List(
            fields.String, required=True, description='gui_type of error')
    })
errors = api.model(
    'errors', {
        'errors':
        fields.List(
            fields.Nested(error), required=True, description='list of errors')
    })


@api.route('/')
class UserLogin(Resource):
    @api.response(403, 'Not Authorized', model=errors)
    @api.response(200, 'Authorized', model=success_authenticate)
    @api.doc('create_token')
    @api.expect(user, validate=True)
    @api.doc(params={'payload': 'need data for Authentication'})
    # @ns.marshal_with(user, code=201)
    def post(self):
        '''create auth'''
        print(api.payload)
        return check_login(api.payload['username'], api.payload['password'])
