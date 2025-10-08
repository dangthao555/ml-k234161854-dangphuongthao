import traceback

import  mysql.connector

server="localhost"
port=3306
database="k23416_retail"
username="root"
password="@Obama123"

try:
    conn = mysql.connector.connect(
                    host=server,
                    port=port,
                    database=database,
                    user=username,
                    password=password)
except:
    traceback.print_exc()
print("--Tiếp tục phần mềm--")
print("--CRUD--")
# Câu 1: Đăng nhập cho customer
def login_customer(email, password):
    cursor = conn.cursor()
    sql = "SELECT * FROM customer " \
          " WHERE email='"+email +"' AND password='"+password+"'"
    print(sql)
    cursor.execute(sql)

    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("Login failed")
    cursor.close()

login_customer("daodao@gmail.com", "123")

def login_employee(email, password):
    cursor = conn.cursor()
    sql = "SELECT * FROM employee " \
          "WHERE email=%s and password=%s"
    val=(email, password)
    cursor.execute(sql, val)
    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("Login failed")
    cursor.close()

login_employee("kim@yahoo.com", "123")