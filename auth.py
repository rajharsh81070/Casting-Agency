import os
import json
from flask import request, _request_ctx_stack, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen


'''
Variables for executing the app locally
    AUTH0_DOMAIN = 'fsnd-harsh-capstone.us.auth0.com'
    ALGORITHMS = 'RS256'
    API_AUDIENCE = 'cagency'
'''


AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
ALGORITHMS = os.environ.get('ALGORITHMS')
API_AUDIENCE = os.environ.get('API_AUDIENCE')


'''
AuthError Exception:
A standardized way to communicate auth failure modes
'''


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


'''
Implemented get_token_auth_header() method:
    - It gets the header from the request
    - It obtains Access Token from Authorization Header
    - It raises an AuthError if no header is present
    - It splits the bearer and the token
    - It raises an AuthError if the header is malformed
    and finally returns the token part of the header
'''


def get_token_auth_header():
    auth = request.headers.get('Authorization', None)
    if not auth:
        raise AuthError({
            'code': 'authorization_header_missing',
            'description': 'Authorization header is expected.'
        }, 401)

    parts = auth.split()
    if parts[0].lower() != 'bearer':
        raise AuthError({
            'code': 'invalid_header',
            'description':
            'Authorization header must start with "Bearer".'
        }, 401)

    elif len(parts) == 1:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Token not found.'
        }, 401)

    elif len(parts) > 2:
        raise AuthError({
            'code': 'invalid_header',
            'description':
            'Authorization header must be bearer token.'
        }, 401)

    token = parts[1]
    return token


'''
Implemented the check_permissions(permission, payload) method
@INPUTS
    permission: string permission (example: 'post:actors')
    payload: decoded jwt payload
- It raises an AuthError if permissions are not included in payload
- It raises an AuthError if requested permission string is not in
  the payload permissions array
- Returns true otherwise
'''


def check_permissions(permission, payload):
    if 'permissions' not in payload:
        raise AuthError({
            'code': 'invalid_claims',
            'description': 'Permissions not included in JWT.'
        }, 400)

    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'unauthorized',
            'description': 'Permission not found.'
        }, 403)
    return True


'''
Implemented verify_decode_jwt(token) method
@INPUTS
    token: a json web token (string)

- It will be an Auth0 token with key id (kid)
- It will verify the token using Auth0 /.well-known/jwks.json
- It will decode the payload from the token
- It will validate the claims
- Returns the decoded payload
'''


def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description':
                    'Incorrect claims.   \
                    Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
        'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
    }, 400)


'''
Implemented @requires_auth(permission) decorator method
@INPUTS
    permission: string permission (example: 'post:actors')

- It will use the get_token_auth_header method to get the token
- It will use the verify_decode_jwt method to decode the jwt
- It will use the check_permissions method validate claims and
  check the requested permission
- Returns the decorator which passes the decoded payload to the
  decorated method
'''


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator
