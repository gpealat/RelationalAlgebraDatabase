import csv
import sqlite3
import configparser
from database.db_creation import create_db_path

config = configparser.ConfigParser()
config.read('SETUP.INI')

def fill_cinema_table():
    """Function that fills the CINEMA table with data
    """
    cinema_file = f'./{config["DATA"]["Folder"]}/cinemas.csv'

    # Read the cinema file
    with open(cinema_file, newline='') as csvfile:
        cinemareader = csv.reader(csvfile, delimiter=",")

        db_path = create_db_path()

        con = sqlite3.connect(db_path)
        cur = con.cursor()

        # For each actor add it in the table
        for cinema in cinemareader:
            sql = ''' INSERT INTO CINEMA(CinemaName,Phone,Street) VALUES (?,?,?); '''
            cur.execute(sql, cinema)
            
        con.commit()
        con.close()
