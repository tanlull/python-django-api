import mysql.connector as mysql

def deleteData(id):
   try:
       conn = mysql.connect(user='root', password='toor',
                host='127.0.0.1', database='api')
       cursor = conn.cursor()
       # Update single record now
       sql_delete_query = "Delete from source where id = %s"
       cursor.execute(sql_delete_query, (id,))
       conn.commit()
       count = cursor.rowcount
       print(count, "Record deleted successfully ")
   except (Exception, pg.Error) as error:
       print("Error in Delete operation", error)
   finally:
       # closing database conn.
       if (conn):
           cursor.close()
           conn.close()
           print("PostgreSQL conn is closed")

deleteData(10)

