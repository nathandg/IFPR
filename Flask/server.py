""" Flask Simple Server"""

import json
from flask import Flask, request
from services.user_service import add_user, get_user, get_users

app = Flask(__name__)


@app.route('/add', methods=['POST'])
def create_user():
    """ Create user """
    content_type = request.headers.get('Content-Type')
    print('Content Type', content_type)
    if content_type == 'application/json':
        data = request.json
        if add_user(data):
            return app.response_class(
                response=json.dumps({'user': data}),
                status=201,
                mimetype='application/json'
            )
        else:
            return app.response_class(
                response=json.dumps({'message': 'User already exists'}),
                status=400,
                mimetype='application/json'
            )
    else:
        return app.response_class(
            response=json.dumps({'message': 'Invalid Content Type'}),
            status=400,
            mimetype='application/json'
        )


@app.route('/users')
def get_all_users():
    """ Get all users """
    return app.response_class(
        response=json.dumps({'users': get_users()}),
        status=200,
        mimetype='application/json'
    )

# Get user by CPF using Query parameters
@app.route('/user')
def get_user_by_cpf():
    """ Get user by CPF """
    cpf = request.args.get('cpf')
    print('CPF', cpf)
    user = get_user(cpf)
    if user:
        return app.response_class(
            response=json.dumps({'user': user}),
            status=200,
            mimetype='application/json'
        )
    else:
        return app.response_class(
            response=json.dumps({'message': 'User not found'}),
            status=404,
            mimetype='application/json'
        )
