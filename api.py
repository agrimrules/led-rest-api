__author__ = 'agrimasthana'
from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
from flask_api import status
from os import system

app = Flask(__name__)
mySql = MySQL()

config = {}
execfile("settings.conf", config)

app.config['MYSQL_DATABASE_USER'] = config['user']
app.config['MYSQL_DATABASE_PASSWORD'] = config['password']
app.config['MYSQL_DATABASE_DB'] = config['database']
app.config['MYSQL_DATABASE_HOST'] = config['host']
mySql.init_app(app)

conn = mySql.connect()

@app.route("/led", methods=['POST'])
def led():
    print(request)
    _message = request.json['message']
    try:
        cursor = conn.cursor()
        cursor.execute("insert into Messages(message) values (%s)", _message)
        conn.commit()
        system('python ledbadge.py effect=left speed=5 "'+_message+'"')
        cursor.close()
    except conn.IntegrityError:
        return jsonify({'status': 'Failed'}), status.HTTP_500_INTERNAL_SERVER_ERROR
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
