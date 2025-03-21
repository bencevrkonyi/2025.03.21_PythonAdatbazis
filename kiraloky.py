from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='',
                                 host='127.0.0.1',
                                 database='kiralyok')

cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

cnx.close()