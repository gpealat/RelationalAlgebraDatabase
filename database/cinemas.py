import csv
import sqlite3

def fill_cinema_table():
    cinema_file = "./data/cinemas.csv"

    # Read the cinema file
    with open(cinema_file, newline='') as csvfile:
        cinemareader = csv.reader(csvfile, delimiter=",")

        con = sqlite3.connect("./database/sql_exercices.db")
        cur = con.cursor()

        # For each actor add it in the table
        for cinema in cinemareader:
            sql = ''' INSERT INTO CINEMA(CinemaName,Phone,Street) VALUES (?,?,?); '''
            cur.execute(sql, cinema)
            
        con.commit()
        con.close()
