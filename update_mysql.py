import mysql.connector as mysql

def updateTable(id, newid):
    try:
        conn = mysql.connect(user='root', password='toor',
                             host='127.0.0.1', database='api')
        cursor = conn.cursor()
        sql_update = "Update source set id = %s where id = %s"""
        cursor.execute(sql_update, (newid, id))
        conn.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")
    except (Exception, pg.Error) as error:
        print("Error in update operation", error)
    finally:
        # closing database conn.
        if (conn):
            cursor.close()
            conn.close()
            print("PostgreSQL conn is closed")

updateTable(5, 10)