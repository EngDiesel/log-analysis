#!/usr/bin/env python3

__author__ = "Mostafa Yasin"
__copyright__ = "Copyright (C) 2018 Mostafa Yasin"
__license__ = "Public Domain"
__version__ = "1.0"

# importing modules.
import psycopg2
import os
import sys

# declearing global variables
db_name = 'news'


# start the connection
def Connect(database_name):

    """
        This function starts a new connection with
        the 'news' database
    """
    try:
        return psycopg2.connect(dbname=database_name)
    except psycopg2.Error as e:
        error_message = 'We are sorry for that but we can\
         not connect to database with this error... \n' + str(e)
        return error_message


def get_most_popular_articles():
    """
    Returns most popular articles.
    """
    res = []
    conn = Connect(db_name)
    cursor = conn.cursor()

    query = """select articles.title, count(log.ip) as views
    from log join articles
    on log.path = concat('/article/', articles.slug)
    group by articles.title
    order by views desc limit 3;"""

    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    i = 1
    for result in results:
        temp = str(result[0]) + "' -- " + str(result[1])
        obj = "\n" + str(i) + " ) '" + temp + " Views"
        res.append(obj)
        i += 1

    return res


def get_most_popular_articles_authors():
    """
    Returns the most popular articles' authors.
    """
    res = []
    conn = Connect(db_name)
    cursor = conn.cursor()
    query = """
        select authors.name, count(log.ip) as views from log,
        authors, articles where articles.author = authors.id and
        CONCAT('/article/',articles.slug) = log.path
        group by authors.name order by views desc limit 3;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    i = 1
    for result in results:
        temp = str(result[0]) + "' -- " + str(result[1])
        obj = "\n" + str(i) + " ) '" + temp + " Views"
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

    query = """
        select to_char(date, 'FMMonth FMDD, YYYY'),
        (err/total) * 100 as ratio
        from (select time::date as date,
        count(*) as total,
        sum((status != '200 OK')::int)::float as err
        from log group by date) as errors
        where err/total > 0.01;
    """

    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    i = 1
    for result in results:
        temp = str(result[0]) + "' -- " + str(round(result[1], 1))
        obj = "\n" + str(i) + " ) '" + temp + " %"
        res.append(obj)
        i += 1

    return res


def main():

    try:
        outputfile = open('output.txt', 'w')
    except Exception as e:
        print(str(e))

    # Best 3 articles.
    print("\n\n---------------- 1) Most popular three articles of all time ?\
 ----------------")

    outputfile.write("\n\n---------------- \
 1) Most popular three articles of all time ? ----------------")
    res = get_most_popular_articles()
    for obj in res:
        print(obj)
        outputfile.write(obj)

    # Best 3 articles authors
    print('\n\n---------------- 2) Most popular article\
 authors of all time ? ---------------')

    outputfile.write('\n\n---------------- 2) Most popular article\
     authors of all time ? ---------------')
    res = get_most_popular_articles_authors()
    for obj in res:
        print(obj)
        outputfile.write(obj)

    # Log Errors
    print('\n\n------- On which days did more than 1% of\
 requests lead to error ? -----------')

    outputfile.write('\n\n------- On which days did more than 1% of\
 requests lead to error ? -----------')

    res = get_log_error()
    for obj in res:
        print(obj)
        outputfile.write(obj)

    print()
    outputfile.write('\n')
    outputfile.close()


main()
