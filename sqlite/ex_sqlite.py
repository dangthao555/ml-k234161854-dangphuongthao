import sqlite3
import pandas as pd

try:
    # Connect to DB
    sqliteConnection = sqlite3.connect("../databases/Chinook_Sqlite.sqlite")
    cursor = sqliteConnection.cursor()
    print("DB Init")

    n = int(input("Nhập số lượng khách hàng top N: "))

    query = f"""
            SELECT 
                c.CustomerId,
                c.LastName,
                SUM(il.UnitPrice * il.Quantity) AS TotalValue
            FROM Invoice i
            JOIN Customer c ON i.CustomerId = c.CustomerId
            JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
            GROUP BY c.CustomerId
            ORDER BY TotalValue DESC
            LIMIT {n}
    """
    cursor.execute(query)
    df = pd.DataFrame(cursor.fetchall(), columns=["CustomerId","CustomerName","TotalValue"])
    print(df)
    # Close the cursor
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite:", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite connection is closed")
