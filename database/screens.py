import csv
import sqlite3

def fill_screens_table():
    screens_file = "./data/screens.csv"

    # Read the screens file
    with open(screens_file, newline='') as csvfile:
        screenreader = csv.reader(csvfile, delimiter=",")

        con = sqlite3.connect("./database/sql_exercices.db")
        cur = con.cursor()

        # For each movie add it in the table
        for screen in screenreader:
            sql = ''' INSERT INTO SCREEN(CinemaName,ScreenNumber,Phone_Ext,SeatNumber) VALUES (?,?,?,?); '''
            cur.execute(sql, screen)
            
        con.commit()
        con.close()
