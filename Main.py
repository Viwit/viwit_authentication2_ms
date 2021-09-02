# export FLASK_APP=Main.py
# flask run -h localhost -p 8081
# sudo usermod -aG docker ${USER}
# su - ${USER}
# docker system prune -a
# docker build -t authentication2 .
# docker run --network='host' -p 4000:4000 authentication2
import sys

import blockAccount
import Token
from flask import Flask
from flask import request
import requests

import connectionDB

import json

app = Flask(__name__)

errorMethod = "405 Method Not Allowed", 405

@app.route('/login/<email>/<password>', methods=['GET'])
def login(email, password):
    try:
        sql = "SELECT * FROM users WHERE email ='" + email + "' and user_password ='" + password + "'"

        connection = connectionDB.open_connection()
        connection_cursor = connection.cursor()
        connection_cursor.execute(sql)

        result = connection_cursor.fetchall()
        '''state = {
            "user_id": result[0][0],
            "firstname": result[0][1],
            "lastname": result[0][2],
            "email": result[0][3],
            "reg_date": result[0][4],
            "user_password": result[0][5],
            "wallet_id": result[0][6],
            "block_account": result[0][7],
            "user_type": result[0][8]
        }'''

        connection_cursor.close()
        connection.close()
        if len(result) > 1:
            return {"error 1": "HAVE 2 RESULTS wtf?"}, 500
        return {"isLogin": len(result), "user_id": result[0][0]}, 200
    except:
        return {"isLogin": "0", "user_id": 0, "error 1": str(sys.exc_info()[0]), "error 2": str(sys.exc_info()[1])}


@app.route('/hello', methods=['GET'])
def hello():
    if request.method == 'GET':
        connection = connectionDB.open_connection()
        connection.close()
        return blockAccount.hello()
    else:
        global errorMethod
        return errorMethod


@app.route('/update-blockAccount/<id_user>', methods=['PUT'])
def block_account(id_user):
    if request.method == 'PUT':
        return blockAccount.block_account(id_user)
    else:
        global errorMethod
        return errorMethod


@app.route('/update-unlockAccount/<id_user>', methods=['PUT'])
def unlock_account(id_user):
    if request.method == 'PUT':
        return blockAccount.unlock_account(id_user)
    else:
        global errorMethod
        return errorMethod


'''
@app.route('/token', methods=['GET'])
def token():
    if request.method == 'GET':
        return Token.get_tokens();
    else:
        global errorMethod
        return errorMethod
'''


@app.route('/token/<id>/<arg>', methods=['PUT', 'GET', 'POST', 'DELETE'])
def token_id(id, arg):
    if request.method == 'PUT':
        return Token.put_token(id, arg)
    elif request.method == 'POST':
        return Token.post_token(id, arg)
    elif request.method == 'DELETE':
        return Token.delete_token(id, arg)
    else:
        global errorMethod
        return errorMethod


@app.route('/token-firebase/<id>/<firebase>', methods=['PUT', 'GET', 'POST', 'DELETE'])
def token_firebase(id, firebase):
    if request.method == 'POST':
        data = Token.post_token(id, "Login")
        return Token.put_token_firebase(id, data[0]["token"], firebase)
    else:
        global errorMethod
        return errorMethod


@app.route('/token-firebase/<id>', methods=['PUT', 'GET', 'POST', 'DELETE'])
def token_firebase_get(id):
    if request.method == 'GET':
        return Token.get_token_firebase(id)
    else:
        global errorMethod
        return errorMethod


