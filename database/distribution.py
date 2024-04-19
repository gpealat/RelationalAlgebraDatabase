import csv
import sqlite3
import configparser
from database.db_creation import create_db_path

config = configparser.ConfigParser()
config.read('SETUP.INI')

def fill_distribution_table():
    """Function that fills the DISTRIBUTION table with data
    """
    distribution_file = f'./{config["DATA"]["Folder"]}/distribution.csv'

    # Read the distribution file
    with open(distribution_file, newline='') as csvfile:
        distributionreader = csv.reader(csvfile, delimiter=",")

        db_path = create_db_path()

        con = sqlite3.connect(db_path)
        cur = con.cursor()

        # For each distribution add it in the table
        for d in distributionreader:
            sql = ''' INSERT INTO DISTRIBUTION(Title,ActorName,NbOfPlayedScences) VALUES (?,?,?); '''
            cur.execute(sql, d)
            
        con.commit()
        con.close()