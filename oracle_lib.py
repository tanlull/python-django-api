import cx_Oracle as ora
conn = {}
cursor = {}

def connect():
    global conn, cursor
    try:
        #conn = ora.connect('train00','train00','dboda-scan.rubber.co.th/testrac')
        conn = ora.connect('train00','train00','localhost/orcl')
        cursor = conn.cursor()
        return True
    except (Exception, ora.Error) as error:
        print("Error ", error)
        return False

def close():
    global conn, cursor
    if(conn):
        cursor.close()
        conn.close()
        print("----  closed connection --")

def select(sql):
    global conn, cursor
    try:
        cursor.execute(sql)
        data = list2dict(cursor)
        return data
    except (Exception, ora.Error) as error:
        print("Error while fetching data from ora.", error)

def list2dict(cursor):
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data_dict = [dict(zip(column_names, row)) for row in cursor.fetchall()]
    return data_dict

def executeSQL(sql):
    global conn, cursor
    data = {}
    try:
        cursor.execute(sql)
        conn.commit()
        count = cursor.rowcount
        data["status"] = "Success"
        data["count"] = count
        return data
    except (Exception, ora.Error) as error:
        print("Error while fetching data from ora.", error)
        data["status"] = "Error"
        data["message"] = str(error)
    finally:
        return data
