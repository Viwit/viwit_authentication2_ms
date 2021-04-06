# export FLASK_APP=blockAccount.py
# flask run -h localhost -p 8081
# sudo usermod -aG docker ${USER}
# su - ${USER}
# docker system prune -a
# docker build -t archit  archit
# docker run archit


import connectionDB
from flask import Flask

app = Flask(__name__)
connection = connectionDB.connect()
connection_cursor = connection.cursor()


@app.route('/hello')
def hello():
    return "HELLO", 200


@app.route('/update-blockAccount/<id_user>')
def block_account(id_user):
    sql = "UPDATE user_viwit SET `block_account`='1', `credit_card`='1' WHERE user_id ='" + id_user + "';"
    connection_cursor.execute(sql)
    connection.commit()
    return "OK", 200
    try:
        pass
    except:
        return 'Database connection failed', 500


@app.route('/update-unlockAccount/<id_user>')
def unlock_account(id_user):
    try:
        sql = "UPDATE user_viwit SET `block_account`='0' WHERE user_id ='" + id_user + "';"
        connection_cursor.execute(sql)
        connection.commit()
        return "OK", 200
    except:
        return 'Database connection failed', 500
