
import csv
import sqlite3

def fill_programs_table():
    programs_file = "./data/programs.csv"

    # Read the distribution file
    with open(programs_file, newline='') as csvfile:
        programreader = csv.reader(csvfile, delimiter=",")

        con = sqlite3.connect("./database/sql_exercices.db")
        cur = con.cursor()

        # For each distribution add it in the table
        for program in programreader:
            sql = ''' INSERT INTO PROGRAM(CinemaName,ScreenNumber,Week, Title, NbOfTicketsSold) VALUES (?,?,?,?,?); '''
            cur.execute(sql, program)
            
        con.commit()
        con.close()