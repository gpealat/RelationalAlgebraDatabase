import csv
import sqlite3

def fill_distribution_table():
    distribution_file = "./data/distribution.csv"

    # Read the distribution file
    with open(distribution_file, newline='') as csvfile:
        distributionreader = csv.reader(csvfile, delimiter=",")

        con = sqlite3.connect("./database/sql_exercices.db")
        cur = con.cursor()

        # For each distribution add it in the table
        for d in distributionreader:
            sql = ''' INSERT INTO DISTRIBUTION(Title,ActorName,NbOfPlayedScences) VALUES (?,?,?); '''
            cur.execute(sql, d)
            
        con.commit()
        con.close()