import csv
import sqlite3
import configparser
from database.db_creation import create_db_path

config = configparser.ConfigParser()
config.read('SETUP.INI')

def fill_movies_table():
    """Function that fills the MOVIE table with data
    """
    movie_file = f'./{config["DATA"]["Folder"]}/movies.csv'

    # Read the movie file
    with open(movie_file, newline='') as csvfile:
        moviereader = csv.reader(csvfile, delimiter=",")

        db_path = create_db_path()
        con = sqlite3.connect(db_path)
        cur = con.cursor()

        # For each movie add it in the table
        for movie in moviereader:
            sql = ''' INSERT INTO MOVIE(Title,Country,Director,Year) VALUES (?,?,?,?); '''
            cur.execute(sql, movie)
            
        con.commit()
        con.close()
