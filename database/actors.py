import csv
import sqlite3
from database.db_creation import create_db_path
import configparser

config = configparser.ConfigParser()
config.read('SETUP.INI')

def fill_actor_table():
    """Function that fills the ACTORS table with data
    """
    # Create the actors file path for the data
    actors_file = f'./{config["DATA"]["Folder"]}/actors.csv'

    # Read the actors file
    with open(actors_file, newline='') as csvfile:
        # Create the CSV reader
        actorreader = csv.reader(csvfile)
        # Get the DB path
        db_path = create_db_path()
        # Connect to the DB
        con = sqlite3.connect(db_path)
        cur = con.cursor()

        # For each actor add it in the table
        for actor in actorreader:
            sql = ''' INSERT INTO ACTORS(ActorName) VALUES (?); '''
            cur.execute(sql, actor)
        # Commit the changes
        con.commit()
        # Close the connection
        con.close()
