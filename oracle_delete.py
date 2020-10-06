import cx_Oracle as ora

def deleteData(id):
   try:
       conn = ora.connect('train00','train00','dboda-scan.rubber.co.th/testrac')
       cursor = conn.cursor()
       # Update single record now
       sql_delete_query = "Delete from source where id = :1"
       cursor.execute(sql_delete_query, (id,))
       conn.commit()
       count = cursor.rowcount
       print(count, "Record deleted successfully ")
   except (Exception, ora.Error) as error:
       print("Error in Delete operation", error)
   finally:
       # closing database conn.
       if (conn):
           cursor.close()
           conn.close()
           print("Oracle conn is closed")

deleteData(10)

