import cx_Oracle as ora

try:
    #Connection
    conn = ora.connect('train00','train00','dboda-scan.rubber.co.th/testrac')
    cursor = conn.cursor()

    #Select from database
    sql = "select * from source"
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        print ("Id = {0} , Name = {1}, Age  = {2}, Gender  = {3}".format(row[0],row[1],row[2],row[3]))

except (Exception, ora.Error) as error :
    print ("Error while fetching data from Oracle.", error)
finally:
    #closing database connection.
    if(conn):
        cursor.close()
        conn.close()
        print("Oracle connection is closed")