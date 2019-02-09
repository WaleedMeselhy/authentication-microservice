"""Main operations."""
import os
from flask import Flask, request, jsonify
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,
                                get_jwt_identity, get_jwt_claims)

from jwt_controller import jwt
app = Flask(__name__)
app.config['JWT_ALGORITHM'] = os.environ['JWT_ALGORITHM']

app.config['JWT_PUBLIC_KEY'] = os.environ['JWT_PUBLIC_KEY'].replace(
    '\\n', '\n')
jwt.init_app(app)

users = [{
    'username': 'test1',
    'password': 'test1',
    'id': '1',
    'admin': True
}, {
    'username': 'test2',
    'password': 'test2',
    'id': '2',
    'admin': False
}, {
    'username': 'test3',
    'password': 'test3',
    'id': '3',
    'admin': False
}]


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/login', methods=['POST'])
def login():
    """Check username and passwod."""
    data = request.json
    for user in users:
        if (data['username'] == user['username']
                and data['password'] == user['password']):
            return jsonify({
                'identity': user['id'],
                'claims': {
                    'admin': user['admin']
                }
            })
    return ('error in login'), 400


@app.route('/change_password', methods=['POST'])
@jwt_required
def change_password():
    """Change password."""
    data = request.json
    for user in users:
        if (data['username'] == user['username']):
            user['password'] = data['password']
            return (''), 200


@app.route('/delete_user', methods=['DELETE'])
@jwt_required
def delete_user():
    """Delete user."""
    data = request.json
    claims = get_jwt_claims()
    if not claims['admin']:
        return 'not admin', 400
    for index, user in enumerate(users):
        if (data['username'] == user['username']):
            del users[index]
            return (''), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
