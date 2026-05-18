
# database.py 
# centeralizes and manages database connections
import sqlite3

def get_db_connection():
    # create ashinaga.db if it doesn't exist. Then, create the sqlite connection object
    conn = sqlite3.connect("ashinaga.db")

    # changes the tuple-style results into python dict-style results
    # so, we can access by their 'key', no by their index, which are forgotable.
    conn.row_factory = sqlite3.Row

    # return the connection object
    return conn
   