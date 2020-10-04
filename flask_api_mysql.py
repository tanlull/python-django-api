from flask import Flask, request, jsonify
import itertools
import mysql_lib 
app = Flask(__name__)

def get_all():
    mysql_lib.connect()
    sql = "select * from source"
    data = mysql_lib.select(sql)
    mysql_lib.close()
    return data

def get_by_id(id):
    mysql_lib.connect()
    sql = "select * from source where id={}".format(id)
    print(sql)
    data = mysql_lib.select(sql)
    mysql_lib.close()
    return data

@app.route('/all', methods=['POST','GET']) 
def all():
    result = get_all()
    return jsonify(result)

@app.route('/by_id', methods=['POST','GET']) 
def by_id():
    data = request.args
    id = data["id"]
    result = get_by_id(id)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')




