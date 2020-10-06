import cx_Oracle as ora

def updateTable(id, newid):
    try:
        conn = ora.connect('train00','train00','dboda-scan.rubber.co.th/testrac')
        cursor = conn.cursor()
        sql_update = "Update source set id = :1 where id = :2"
        cursor.execute(sql_update, (newid, id))
        conn.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")
    except (Exception, ora.Error) as error:
        print("Error in update operation", error)
    finally:
        # closing database conn.
        if (conn):
            cursor.close()
            conn.close()
            print("ORacle conn is closed")

updateTable(5, 10)