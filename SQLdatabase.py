import sqlite3

connection = sqlite3.connect('logindata.sqlite')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE ids (
               id TEXT NOT NULL,
               email TEXT NOT NULL,
               senha TEXT NOT NULL)""")

connection.commit()
print("OK")
connection.close()
