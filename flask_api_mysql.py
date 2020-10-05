from flask import Flask, request, jsonify
import mysql_lib 
app = Flask(__name__)

# Select ALL
@app.route('/all', methods=['GET']) 
def all():
    result = db_get_all()
    return jsonify(result)

def db_get_all():
    mysql_lib.connect()
    sql = "select * from source"
    data = mysql_lib.select(sql)
    mysql_lib.close()
    return data

# Select By ID
@app.route('/by_id', methods=['GET']) 
def by_id():
    data = request.args
    print(request.method)
    id = data["id"]
    result = db_get_by_id(id)
    return jsonify(result)

def db_get_by_id(id):
    mysql_lib.connect()
    sql = "select * from source where id={}".format(id)
    print(sql)
    data = mysql_lib.select(sql)
    mysql_lib.close()
    return data

# Insert
@app.route('/insert', methods=['POST']) 
def insert():
    data = request.args
    result = db_insert(data["id"],data["name"],data["age"],data["gender"])
    return jsonify(result)

def db_insert(id,name,age,gender):
    mysql_lib.connect()
    insert_sql = "insert into source values('{}','{}','{}','{}')".format(id,name,age,gender)
    print(insert_sql)
    data = mysql_lib.executeSQL(insert_sql)
    mysql_lib.close()
    return data

# Update
@app.route('/update', methods=['PUT']) 
def update():
    data = request.args
    result = db_update(data["id"],data["name"])
    return jsonify(result)

def db_update(id,name):
    mysql_lib.connect()
    sql = "update source set name='{}' where id ={}".format(name,id)
    print(sql)
    data = mysql_lib.executeSQL(sql)
    mysql_lib.close()
    return data

# Delete
@app.route('/delete', methods=['DELETE']) 
def delete():
    data = request.args
    result = db_delete(data["id"])
    return jsonify(result)

def db_delete(id):
    mysql_lib.connect()
    sql = "delete from source where id ={}".format(id)
    print(sql)
    data = mysql_lib.executeSQL(sql)
    mysql_lib.close()
    return data



if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')




