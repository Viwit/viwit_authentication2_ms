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

app = Flask(__name__)


@app.route('/hello')
def hello():
    return blockAccount.hello()


@app.route('/update-blockAccount/<id_user>')
def block_account(id_user):
    return blockAccount.block_account(id_user)


@app.route('/update-unlockAccount/<id_user>')
def unlock_account(id_user):
    return blockAccount.unlock_account(id_user)


@app.route('/update-token/<id>')
def update_token(id):
    return Token.update_token(id)


@app.route('/read-token/<id>')
def read_token(id):
    return Token.read_token(id)


@app.route('/create-token/')
def create_token():
    return Token.create_token()
