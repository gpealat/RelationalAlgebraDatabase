# MOVIE (Title, Country, Director, Year)

import csv
import sqlite3

def fill_movies_table():
    movie_file = "./data/movies.csv"

    # Read the movie file
    with open(movie_file, newline='') as csvfile:
        moviereader = csv.reader(csvfile, delimiter=",")

        con = sqlite3.connect("./database/sql_exercices.db")
        cur = con.cursor()

        # For each movie add it in the table
        for movie in moviereader:
            sql = ''' INSERT INTO MOVIE(Title,Country,Director,Year) VALUES (?,?,?,?); '''
            cur.execute(sql, movie)
            
        con.commit()
        con.close()
