#SQL is built in! No import is needed.
import sqlite3 as sl
connection = sl.connect("rockyou-test.db")

with connection:
    connection.execute("""
        CREATE TABLE ROCKYOU(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            passwords TEXT
        );
        """)

sql = "INSERT INTO ROCKYOU (id, passwords) values (?,?)"
data = [
    (1, "pass1")
    (2, "pass2")
    (3, "pass3")
]
with connection:
    connection.executemany(sql, data)

with connection:
    data_select = connection.execute("SELECT * FROM ROCKYOU")
    for row in data_select:
        print(row)

