__author__ = "Mostafa Yasin"
__copyright__ = "Copyright (C) 2018 Mostafa Yasin"
__license__ = "Public Domain"
__version__ = "1.0"


import psycopg2

db_name = 'news'

def Connect(database_name):
    """
        This function starts a new connection with
        the 'news' database
    """
    try:
        return psycopg2.connect(dbname=database_name)
    except psycopg2.Error as e:
        error_message = 'We are sorry for that but we can not connect to database with this error... \n' + str(e)
        return error_message

conn = Connect(db_name)
print(conn)
