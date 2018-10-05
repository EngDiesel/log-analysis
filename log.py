__author__ = "Mostafa Yasin"
__copyright__ = "Copyright (C) 2018 Mostafa Yasin"
__license__ = "Public Domain"
__version__ = "1.0"

# importing modules.
import psycopg2
import os

# declearing global variables
db_name = 'news'

create_popular_articles = """
    create view popular_articles as
    select articles.title, count(log.ip) as views
    from log join articles
    on log.path = concat('/article/', articles.slug)
    group by articles.title
    order by views desc;
"""

create_popular_articles_authors = """
    create view popular_articles_authors as
    select authors.name, count(log.ip) as views from log,
    authors, articles where articles.author = authors.id and
    CONCAT('/article/',articles.slug) = log.path
    group by authors.name order by views desc;
"""

create_log_error = """
create view log_error as
select to_char(date, 'FMMonth FMDD, YYYY'),
(err/total) * 100 as ratio
from (select time::date as date,
count(*) as total,
sum((status != '200 OK')::int)::float as err
from log group by date) as errors
where err/total > 0.01;
"""

# Clear the console
def clear():
    os.system('clear')

# start the connection
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


# Create views
def create_views():
    """
    This function connects to database and executes queries to
    create views.
    this views helps in other functions.
    """
    conn = Connect(db_name)
    cursor = conn.cursor()
    cursor.execute(create_popular_articles)
    cursor.execute(create_popular_articles_authors)
    cursor.execute(create_log_error)
    conn.close()

def get_most_popular_articles():
    """
    Returns most popular articles.
    """
    res = []
    conn = Connect(db_name)
    cursor = conn.cursor()
    cursor.execute("select * from popular_articles limit 3;")
    results = cursor.fetchall()
    conn.close()
    i = 1
    for result in results:
        obj = "\n" + str(i) + " ) '" +  str(result[0]) + "' -- " + str(result[1]) + " Views"
        res.append(obj)
        i += 1

def get_most_popular_articles_authors():
    """
    Returns the most popular articles' authors.
    """
    res = []
    conn = Connect(db_name)
    cursor = conn.cursor()
    cursor.execute("select * from popular_articles_authors limit 3;")
    results = cursor.fetchall()
    conn.close()
    i = 1
    for result in results:
        obj = "\n" + str(i) + " ) '" +  str(result[0]) + "' -- " + str(result[1]) + " Views"
        res.append(obj)
        i += 1

    return res

def get_log_error():
    """
    Returns the days with log errors more than 1%
    """
    res = []
    conn = Connect(db_name)
    cursor = conn.cursor()
    cursor.execute("select * from log_error;")
    results = cursor.fetchall()
    conn.close()
    i = 1
    for result in results:
        obj = "\n" + str(i) + " ) '" +  str(result[0]) + "' -- " + str(round(result[1], 1)) + " %"
        res.append(obj)
        i += 1

    return res

def main():

    # creating the views
    try:
        create_views()
    except psycopg2.Error as e:
        print('\n---------------------------------------------------\n')
        print(str(e))
        print("---------------------------------------------------")



    # Best 3 articles.
    print('\n\n---------------------------------------------------')
    res = get_most_popular_articles()
    for obj in res:
        print(obj)

     # Best 3 articles authors
    print('\n\n---------------------------------------------------')
    res = get_most_popular_articles_authors()
    for obj in res:
        print(obj)


     # Log Errors
    print('\n\n---------------------------------------------------')
    res = get_log_error()
    for obj in res:
        print(obj)


main()
