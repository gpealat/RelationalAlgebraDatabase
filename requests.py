
import sqlite3

try:
    con = sqlite3.connect("./database/sql_exercices.db")
    cur = con.cursor()

    print("Available tables:")
    for row in cur.execute("SELECT name FROM sqlite_master WHERE type='table'"):
        print(row[0])

    print("")
    print("Enter your SQL command (i.e. SELECT * FROM ACTORS):")
    sql = str(input())

    for row in cur.execute(sql):
        print(row)
except Exception as e:
    print(e)