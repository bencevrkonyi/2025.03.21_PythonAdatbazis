#-----------------------------------------------------------------------------------------------------------
#Előző órai feladatok:
#-----------------------------------------------------------------------------------------------------------

import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password=""
)

mycursor = mydb.cursor()

# adatbázis létrehozása
DATABASE = "mydatabase"

mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")

# adatbázisok mutatása
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

# adatbázis használata
mycursor.execute(f"USE {DATABASE}")

# táblázat létrehozása
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
print("------------------------")

# táblák mutatása
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



#-----------------------------------------------------------------------------------------------------------
#2025.04.04.:
#-----------------------------------------------------------------------------------------------------------

import sqlite3

#Kapcsolódás az adatbázishoz
conn = sqlite3.connect("oscar_movies.db")
cursor = conn.cursor()

#2.feladat
query_2 = """
SELECT ev, cim 
FROM film 
WHERE nyert = 1 
ORDER BY ev;
"""
cursor.execute(query_2)
result_2 = cursor.fetchall()

#3.feladat
query_3 = """
SELECT ev 
FROM film 
GROUP BY ev 
HAVING COUNT(*) >= 10;
"""
cursor.execute(query_3)
result_3 = cursor.fetchall()

#4.feladat
query_4 = """
SELECT cim 
FROM film 
WHERE ev BETWEEN 1939 AND 1945 
AND bemutato IS NOT NULL;
"""
cursor.execute(query_4)
result_4 = cursor.fetchall()

#5.feladat
query_5 = """
SELECT cim 
FROM film 
WHERE nyert = 1 
AND bemutato IS NOT NULL 
AND (strftime('%Y', bemutato) - ev) >= 10;
"""
cursor.execute(query_5)
result_5 = cursor.fetchall()

##6.feladat
query_6 = """
SELECT k.nev, COUNT(*) AS jelolesek_szama, 
       MAX(f.ev) - MIN(f.ev) AS idotartam 
FROM kapcsolat ka
JOIN film f ON ka.filmid = f.id
JOIN keszito k ON ka.keszitoid = k.id
WHERE k.producer = 1
GROUP BY k.nev
HAVING COUNT(*) > 1;
"""
cursor.execute(query_6)
result_6 = cursor.fetchall()

##7.feladat
query_7 = """
SELECT DISTINCT k2.nev 
FROM kapcsolat ka1
JOIN kapcsolat ka2 ON ka1.filmid = ka2.filmid
JOIN keszito k1 ON ka1.keszitoid = k1.id
JOIN keszito k2 ON ka2.keszitoid = k2.id
WHERE k1.nev = 'Clint Eastwood' AND k2.nev <> 'Clint Eastwood';
"""
cursor.execute(query_7)
result_7 = cursor.fetchall()

#8.feladat
query_8 = """
SELECT k.nev 
FROM kapcsolat ka
JOIN film f ON ka.filmid = f.id
JOIN keszito k ON ka.keszitoid = k.id
WHERE k.producer = 1
GROUP BY k.nev
HAVING SUM(CASE WHEN f.bemutato IS NOT NULL THEN 1 ELSE 0 END) = 0;
"""
cursor.execute(query_8)
result_8 = cursor.fetchall()

#Eredmények ki írása
print("2.Nyertes filmek:", result_2)
print("3.Évek legalább 10 jelöléssel:", result_3)
print("4.Második világháborús jelöltek:", result_4)
print("5.Késve bemutatott nyertesek:", result_5)
print("6.Producerek jelölési időtartama:", result_6)
print("7.Clint Eastwood producertársai:", result_7)
print("8.Producerek, akiknél nincs magyar premier:", result_8)

#Kapcsolat bezárása
conn.close()