import mysql.connector as mysql

try:
    #Connection
    conn = mysql.connect(user='root', password='toor',host='127.0.0.1',database='api')
    cursor = conn.cursor()

    #Select from database
    sql = "select * from source"
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        print ("Id = {0} , Name = {1}, Age  = {2}, Gender  = {3}".format(row[0],row[1],row[2],row[3]))

except (Exception, mysql.Error) as error :
    print ("Error while fetching data from Mysql.", error)
finally:
    #closing database connection.
    if(conn):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")