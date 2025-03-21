from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='',
                                 host='127.0.0.1',
                                 database='kiralyok')

# táblák megjelenítése
cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

# uralkodók megjelenítése
cursor.execute("SELECT * FROM uralkodo")
for uralkodo in cursor:
    print(uralkodo)

# mátyás király
cursor.execute("SELECT * FROM uralkodo WHERE uralkodo.nev='I. Mátyás'")
for uralkodo in cursor:
    print(uralkodo)
print("----------------------")

# mátyás király
cursor.execute("SELECT szul,hal FROM uralkodo WHERE uralkodo.nev='I. Mátyás")
for uralkodo in cursor:
    print(uralkodo)
print("----------------------")

cnx.close()
