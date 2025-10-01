import mysql.connector

server = "localhost"
port = 3306
database = "studentmanagement"
username = "root"
password = "@Obama123"

conn = mysql.connector.connect(
    host=server,
    port=port,
    database=database,
    user=username,
    password=password,
)

cursor = conn.cursor()

sql="DELETE from student where ID=14"
cursor.execute(sql)

conn.commit()

print(cursor.rowcount," record(s) affected")