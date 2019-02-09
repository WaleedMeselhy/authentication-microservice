from flask_jwt_extended import (JWTManager, verify_jwt_in_request,
                                create_access_token, get_jwt_claims)
jwt = JWTManager()
