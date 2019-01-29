from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token)
from flask import g
import requests
jwt = JWTManager()


@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    print('g.extra_info_for_claims', g.extra_info_for_claims)
    return {}.update(g.extra_info_for_claims)


def check_login(username, password):
    r = requests.post(
        'http://user-management:5000/login',
        json={
            'username': username,
            'password': password
        })
    if r.status_code == 200:
        response_json = r.json()
        g.extra_info_for_claims = {'aas': 'ss'}
        access_token = create_access_token(
            response_json['identity'], fresh=True)
        refresh_token = create_refresh_token(response_json['identity'])
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 200
    else:
        print('r.status_code', r.status_code)
