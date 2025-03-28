import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password=""
)

mycursor = mydb.cursor()

DATABASE = "mydatabase"

mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mycursor.execute(f"USE {DATABASE}")  