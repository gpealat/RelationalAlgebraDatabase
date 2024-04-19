
import csv
import sqlite3
import configparser
from database.db_creation import create_db_path

config = configparser.ConfigParser()
config.read('SETUP.INI')

def fill_programs_table():
    """Function that fills the PROGRAM table with data
    """
    programs_file = f'./{config["DATA"]["Folder"]}/programs.csv'

    # Read the distribution file
    with open(programs_file, newline='') as csvfile:
        programreader = csv.reader(csvfile, delimiter=",")

        db_path = create_db_path()
        con = sqlite3.connect(db_path)
        cur = con.cursor()

        # For each distribution add it in the table
        for program in programreader:
            sql = ''' INSERT INTO PROGRAM(CinemaName,ScreenNumber,Week, Title, NbOfTicketsSold) VALUES (?,?,?,?,?); '''
            cur.execute(sql, program)
            
        con.commit()
        con.close()