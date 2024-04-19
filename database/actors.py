import csv
import sqlite3


def fill_actor_table():
    actors_file = "./data/actors.csv"

    # Read the actors file
    with open(actors_file, newline='') as csvfile:
        actorreader = csv.reader(csvfile)

        con = sqlite3.connect("./database/sql_exercices.db")
        cur = con.cursor()

        # For each actor add it in the table
        for actor in actorreader:
            sql = ''' INSERT INTO ACTORS(ActorName) VALUES (?); '''
            cur.execute(sql, actor)

        con.commit()
        con.close()
