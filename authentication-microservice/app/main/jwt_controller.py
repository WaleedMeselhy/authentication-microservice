"""Jwt controller."""
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token)
from flask import g
import requests
jwt = JWTManager()


@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    """Addimg claims to token."""
    return g.extra_info_for_claims


def check_login(username, password):
    """Check username and passwod."""
    respone = requests.post(
        'http://user-management:5000/login',
        json={
            'username': username,
            'password': password
        })
    if respone.status_code == 200:
        response_json = respone.json()
        g.extra_info_for_claims = response_json['claims']
        access_token = create_access_token(
            response_json['identity'], fresh=True)
        refresh_token = create_refresh_token(response_json['identity'])
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 200
    else:
        return {
            "errors": [{
                "code": 0,
                "message": "username or password error",
                "message_type": "erorr",
                "gui_type": ["pop"]
            }]
        }, 403
