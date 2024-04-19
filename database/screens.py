import csv
import sqlite3
import configparser
from database.db_creation import create_db_path

config = configparser.ConfigParser()
config.read('SETUP.INI')

def fill_screens_table():
    """Function that fills the SCREEN table with data
    """
    screens_file = f'./{config["DATA"]["Folder"]}/screens.csv'

    # Read the screens file
    with open(screens_file, newline='') as csvfile:
        screenreader = csv.reader(csvfile, delimiter=",")

        db_path = create_db_path()
        con = sqlite3.connect(db_path)
        cur = con.cursor()

        # For each movie add it in the table
        for screen in screenreader:
            sql = ''' INSERT INTO SCREEN(CinemaName,ScreenNumber,Phone_Ext,SeatNumber) VALUES (?,?,?,?); '''
            cur.execute(sql, screen)
            
        con.commit()
        con.close()
