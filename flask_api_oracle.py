from flask import Flask, request, jsonify
import oracle_lib 
app = Flask(__name__)


# Select ALL
@app.route('/all', methods=['GET']) 
def all():
    result = db_get_all()
    return jsonify(result)

def db_get_all():
    oracle_lib.connect()
    sql = "select * from source"
    data = oracle_lib.select(sql)
    oracle_lib.close()
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
    oracle_lib.connect()
    sql = "select * from source where id={}".format(id)
    print(sql)
    data = oracle_lib.select(sql)
    oracle_lib.close()
    return data

# Insert
@app.route('/insert', methods=['POST']) 
def insert():
    data = request.args
    result = db_insert(data["id"],data["name"],data["age"],data["gender"])
    return jsonify(result)

def db_insert(id,name,age,gender):
    oracle_lib.connect()
    insert_sql = "insert into source values('{}','{}','{}','{}')".format(id,name,age,gender)
    print(insert_sql)
    data = oracle_lib.executeSQL(insert_sql)
    oracle_lib.close()
    return data

# Update
@app.route('/update', methods=['PUT']) 
def update():
    data = request.args
    result = db_update(data["id"],data["name"])
    return jsonify(result)

def db_update(id,name):
    oracle_lib.connect()
    sql = "update source set name='{}' where id ={}".format(name,id)
    print(sql)
    data = oracle_lib.executeSQL(sql)
    oracle_lib.close()
    return data

# Delete
@app.route('/delete', methods=['DELETE']) 
def delete():
    result ={}
    data = request.args
    allow = authen(request.headers)
    if (allow==False):
        result["status"] = "Error"
        result["message"] = "You don't have privilege!"
    else:
        result = db_delete(data["id"])
    return jsonify(result)

def db_delete(id):
    oracle_lib.connect()
    sql = "delete from source where id ={}".format(id)
    print(sql)
    data = oracle_lib.executeSQL(sql)
    oracle_lib.close()
    return data

token_access = "123456789" # releated to user in database

def authen(headers):
    allow_access = False
    try:
        token = headers["token"]
        print(token)
        if(str(token)==token_access):
            allow_access = True
    except (Exception) as error:
        print(str(error))
    return allow_access

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')




