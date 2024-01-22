import mysql.connector

my = mysql.connector.connect(
    host="http://tolumichael.mysql.pythonanywhere-services.com",
    user="Tolumichael",
    passwd="wS.4j8q9CmXv.!m")

my_cursor = my.cursor()

my_cursor.execute("CREATE DATABASE Tolumichael$excel_db")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)