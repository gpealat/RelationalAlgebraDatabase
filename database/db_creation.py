import sqlite3

def create_db():
    con = sqlite3.connect("./database/sql_exercices.db")

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

    # Missing table ACTORS(ActorName)
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
    con.commit()
    con.close()