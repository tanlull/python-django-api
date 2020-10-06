import cx_Oracle as ora
conn = {}
cursor = {}

def connect():
   global conn,cursor
   try:
       conn = ora.connect('train00','train00','dboda-scan.rubber.co.th/testrac')
       cursor = conn.cursor()
       return True
   except (Exception, ora.Error) as error:
       print("Error ", error)
       return False

def close():
   global conn,cursor
   if(conn):
       cursor.close()
       conn.close()
       print("----  closed connection --")

def selectAll():
   global conn,cursor
   try:
       sql = "select * from source"
       cursor.execute(sql)
       records = cursor.fetchall()
       for row in records:
           print ("Id = {0} , Name = {1}, Age  = {2}, Gender  = {3}".format(row[0],row[1],row[2],row[3]))
   except (Exception, ora.Error) as error :
       print ("Error while fetching data from ora.", error)


def insert(data_to_insert):
   global conn,cursor
   try:
       insert_sql = "insert into source values(:1,:2,:3,:4)"
       #data_to_insert = (5, 'สมเจตน์', 25,'male')
       cursor.execute(insert_sql,data_to_insert)
       conn.commit()
       count = cursor.rowcount
       print(count, "Record Insert successfully ")
   except (Exception, ora.Error) as error :
       print ("Error while fetching data from ora.", error)

def updateTable(id, newid):
   global conn,cursor
   try:
       sql_update = "Update source set id = :1 where id = :2"
       cursor.execute(sql_update, (newid,id))
       conn.commit()
       count = cursor.rowcount
       print(count, "Record Updated successfully ")
   except (Exception, ora.Error) as error:
       print("Error in update operation", error)

def deleteData(id):
   global conn,cursor
   try:
       cursor = conn.cursor()
       sql_delete_query = "Delete from source where id = :1"
       cursor.execute(sql_delete_query, (id,))
       conn.commit()
       count = cursor.rowcount
       print(count, "Record deleted successfully ")
   except (Exception, ora.Error) as error:
       print("Error in Delete operation", error)


