from database.actors import fill_actor_table
from database.cinemas import fill_cinema_table
from database.db_creation import create_db
from database.distribution import fill_distribution_table
from database.movies import fill_movies_table
from database.programs import fill_programs_table
from database.screens import fill_screens_table

# DB initialization. If the DB exists, it will first delete it
create_db()
# Fillinf the ACTOR table
fill_actor_table()
# Filling the CINEMA table
fill_cinema_table()
# Filling the MOVIE table
fill_movies_table()
# Filling the DISTRIBUTION table
fill_distribution_table()
# Fillinf the SCREEN table
fill_screens_table()
# Filling the PROGRAM table
fill_programs_table()