""" Flask Simple Server"""

import json
from flask import Flask, request, render_template
from services.user_service import add_user, get_user, get_users, delete_user

app = Flask(__name__)


@app.route('/')
def index():
    """ Index """
    return render_template('index.html')


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


@app.route('/user')
def get_user_by_cpf():
    """ Get user by CPF using Query parameters """
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


@app.route('/user/<cpf>')
def get_user_by_cpf_path(cpf):
    """ Get user by CPF using Path parameters """
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


@app.route('/user/<cpf>', methods=['DELETE'])
def delete_user_by_cpf(cpf):
    """ Delete user by CPF """
    if delete_user(cpf):
        return app.response_class(
            response=json.dumps({'message': 'User deleted'}),
            status=200,
            mimetype='application/json'
        )
    else:
        return app.response_class(
            response=json.dumps({'message': 'User not found'}),
            status=404,
            mimetype='application/json'
        )


""" TODO - Need to move to separate file """


@app.route('/oz_to_grams')
def oz_to_grams():
    """ Convert oz to grams """
    if request.args.get('oz'):
        oz = float(request.args.get('oz'))
        grams = oz * 28.3495
        return app.response_class(
            response=json.dumps({'grams': grams}),
            status=200,
            mimetype='application/json'
        )

    return app.response_class(
        response=json.dumps(
            {'message': 'Invalid request, please provide oz as query parameter'}),
        status=400,
        mimetype='application/json'
    )


@app.route('/grams_to_oz')
def grams_to_oz():
    """ Convert grams to oz """
    if request.args.get('grams'):
        grams = float(request.args.get('grams'))
        oz = grams / 28.3495
        return app.response_class(
            response=json.dumps({'oz': oz}),
            status=200,
            mimetype='application/json'
        )

    return app.response_class(
        response=json.dumps(
            {'message': 'Invalid request, please provide grams as query parameter'}),
        status=400,
        mimetype='application/json'
    )


@app.route('/is_student_approved', methods=['post'])
def is_student_approved():
    """ Return if student is approved """
    data = request.get_json()
    
    notas = data.get('notas')
    media = (notas[0] + notas [1] + notas[2] + notas[3]) / 4
    print('Media: ', media)

    frequencia = data.get('frequencia')
    print('Frequencia: ', frequencia)

    if media >= 7 and frequencia >= 75:
      return 'Aprovado media: ' + str(media) + ' , e frequencia: ' + str(frequencia)
    
    return 'Reprovado media: ' + str(media) + ' , e frequencia: ' + str(frequencia)
