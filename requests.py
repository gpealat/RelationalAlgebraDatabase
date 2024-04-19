
import sqlite3


con = sqlite3.connect("./database/sql_exercices.db")
cur = con.cursor()

sql = """SELECT *
FROM DISTRIBUTION AS D
WHERE D.Title = (SELECT Title
FROM MOVIE M
WHERE M.Director = 'Luc Besson')
"""
for row in cur.execute(sql):
    print(row)