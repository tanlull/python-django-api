import cx_Oracle as ora

try:
    #Connection
    conn = ora.connect('train00','train00','dboda-scan.rubber.co.th/testrac')
    cursor = conn.cursor()

    #Select
    insert_sql = "insert into source values(:1,:2,:3,:4)"
    data_to_insert = (5, 'สมหมาย', 25,'male')
    cursor.execute(insert_sql, data_to_insert)
    conn.commit()
    count = cursor.rowcount
    print (count, "Record inserted successfully into source table")
    
except (Exception, ora.Error) as error :
    if(conn):
        print("Failed to insert record into source table", error)
finally:
#closing database connection.
    if(conn):
        cursor.close()
        conn.close()
        print("Oracle connection is closed")