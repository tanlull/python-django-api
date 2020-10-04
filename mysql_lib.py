import mysql.connector as mysql
conn = {};
cursor = {};
def connect():
   global conn,cursor
   try:
       conn = mysql.connect(user='root', password='toor',
                              host='127.0.0.1',
                              database='api')
       cursor = conn.cursor()
       return True
   except (Exception, mysql.Error) as error:
       print("Error ", error)
       return False

def close():
   global conn,cursor
   if(conn):
       cursor.close()
       conn.close()
       print("----  closed connection --")

def select(sql):
   global conn,cursor
   try:
        cursor.execute(sql)
        data = list2dict(cursor)
        return data
   except (Exception, mysql.Error) as error :
       print ("Error while fetching data from Mysql.", error)

def insert(data_to_insert):
   global conn,cursor
   try:
       insert_sql = "insert into source values(%s,%s,%s,%s)"
       #data_to_insert = (5, 'สมเจตน์', 25,'male')
       cursor.execute(insert_sql, data_to_insert)
       conn.commit()
       count = cursor.rowcount
   except (Exception, mysql.Error) as error :
       print ("Error while fetching data from Mysql.", error)

def updateTable(id, newid):
   global conn,cursor
   try:
       sql_update = "Update source set id = %s where id = %s"""
       cursor.execute(sql_update, (newid,id))
       conn.commit()
       count = cursor.rowcount
       print(count, "Record Updated successfully ")
   except (Exception, mysql.Error) as error:
       print("Error in update operation", error)

def deleteData(id):
   global conn,cursor
   try:
       cursor = conn.cursor()
       sql_delete_query = "Delete from source where id = %s"
       cursor.execute(sql_delete_query, (id,))
       conn.commit()
       count = cursor.rowcount
       print(count, "Record deleted successfully ")
   except (Exception, mysql.Error) as error:
       print("Error in Delete operation", error)




# convert mysql recordlist to dict
def list2dict(cursor):
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data_dict = [dict(zip(column_names, row)) for row in cursor.fetchall()]
    return data_dict