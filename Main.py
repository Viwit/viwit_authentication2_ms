# export FLASK_APP=Main.py
# flask run -h localhost -p 8081
# sudo usermod -aG docker ${USER}
# su - ${USER}
# docker system prune -a
# docker build -t authentication2 .
# docker run --network='host' -p 4000:4000 authentication2

import blockAccount
import Token
from flask import Flask
from flask import request

app = Flask(__name__)

errorMethod = "405 Method Not Allowed", 405


@app.route('/hello', methods=['GET'])
def hello():
    if (request.method == 'GET'):
        return blockAccount.hello()
    else:
        global errorMethod
        return errorMethod


@app.route('/update-blockAccount/<id_user>', methods=['PUT'])
def block_account(id_user):
    if (request.method == 'PUT'):
        return blockAccount.block_account(id_user)
    else:
        global errorMethod
        return errorMethod


@app.route('/update-unlockAccount/<id_user>', methods=['PUT'])
def unlock_account(id_user):
    if (request.method == 'PUT'):
        return blockAccount.unlock_account(id_user)
    else:
        global errorMethod
        return errorMethod


@app.route('/update-token/<id>', methods=['PUT'])
def update_token(id):
    if (request.method == 'PUT'):
        return Token.update_token(id)
    else:
        global errorMethod
        return errorMethod


@app.route('/read-token/<id>', methods=['GET'])
def read_token(id):
    if (request.method == 'GET'):
        return Token.read_token(id)
    else:
        global errorMethod
        return errorMethod


@app.route('/create-token/<id>', methods=['POST'])
def create_token(id):
    if (request.method == 'POST'):
        return Token.create_token(id)
    else:
        global errorMethod
        return errorMethod
