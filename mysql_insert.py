import mysql.connector as mysql

try:
    #Connection
    conn = mysql.connect(user='root', password='toor',host='127.0.0.1',database='api')
    cursor = conn.cursor()

    #Select
    insert_sql = "insert into source values(%s,%s,%s,%s)"
    data_to_insert = (5, 'สมหมาย', 25,'male')
    cursor.execute(insert_sql, data_to_insert)
    conn.commit()
    count = cursor.rowcount
    print (count, "Record inserted successfully into source table")
    
except (Exception, pg.Error) as error :
    if(conn):
        print("Failed to insert record into source table", error)
finally:
#closing database connection.
    if(conn):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")