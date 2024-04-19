import sqlite3
import os.path
import configparser

config = configparser.ConfigParser()
config.read('SETUP.INI')

def create_db_path()->str:
    return f'./{config["DATABASE"]["Folder"]}/{config["DATABASE"]["Name"]}'

def create_db():
    """Function to initialize the database for the exercises
    """

    # Create the path for the database file
    db_path = create_db_path()

    # Checking if the DB already exists
    if os.path.isfile(db_path):
        # Delete the file
        os.remove(db_path)

    # Create a connection to the DB.
    con = sqlite3.connect(db_path)
    # Create a cursor to run the query
    cur = con.cursor()

    # CINEMA (CinemaName, Phone, Street)
    cur.execute("""CREATE TABLE CINEMA(CinemaName TEXT NOT NULL PRIMARY KEY, 
                                        Phone TEXT,
                                        Street TEXT);""")


    # MOVIE (Title, Country, Director, Year)
    cur.execute("""CREATE TABLE MOVIE(Title TEXT NOT NULL PRIMARY KEY,
                                        Country TEXT,
                                        Director TEXT,
                                        Year INT);""")

    # SCREEN (CinemaName#, ScreenNumber, Phone_Ext, SeatNumber)

    cur.execute("""CREATE TABLE SCREEN(
                    CinemaName TEXT NOT NULL,
                    ScreenNumber INT NOT NULL,
                    Phone_Ext TEXT,
                    SeatNumber INT,
                    PRIMARY KEY (CinemaName, ScreenNumber),
                    FOREIGN KEY (CinemaName) REFERENCES CINEMA(CinemaName)
                );
    """)

    # PROGRAM (CinemaName#, ScreenNumber, Week, Title#, NbOfTicketsSold)
    cur.execute("""CREATE TABLE PROGRAM(
                    CinemaName TEXT NOT NULL ,
                    ScreenNumber INT NOT NULL,
                    Week INT NOT NULL,
                    Title TEXT NOT NULL,
                    NbOfTicketsSold INT,
                    PRIMARY KEY (CinemaName, ScreenNumber, Week),
                    FOREIGN KEY (CinemaName) REFERENCES CINEMA(CinemaName),
                    FOREIGN KEY (Title) REFERENCES MOVIE(Title)
                );
    """)

    # Creating a Missing table ACTORS(ActorName) in the data model
    cur.execute("""CREATE TABLE ACTORS(
                    ActorName TEXT NOT NULL PRIMARY KEY
    );
    """)

    # DISTRIBUTION (Title#, ActorName#, NbOfPlayedScenes)
    cur.execute("""CREATE TABLE DISTRIBUTION(
                    Title TEXT NOT NULL,
                    ActorName TEXT NOT NULL,
                    NbOfPlayedScences INT,
                    PRIMARY KEY (Title, ActorName),
                    FOREIGN KEY (Title) REFERENCES MOVIE(Title),
                    FOREIGN KEY (ActorName) REFERENCES ACTORS(ActorName)
                );
    """)
    # Commit the changes to make them persistent
    con.commit()
    # Close the connection
    con.close()