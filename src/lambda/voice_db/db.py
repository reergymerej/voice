import random as get_random
from connect import get_connection
import psycopg2
from psycopg2.extras import RealDictCursor
import os

def query(fn, sql):
    print("query:", sql)
    if os.getenv('DEV'):
        print("skipping db")
        return
    connection = get_connection()
    cursor = connection.cursor(None, cursor_factory=RealDictCursor)
    # cursor.execute("query with params %s %s", ("param1", "pa'ram2"))
    cursor.execute(sql)
    if fn:
        result = fn(cursor)
    connection.commit()
    connection.close()
    cursor.close()
    return result

def one(sql):
    fn = lambda cursor: cursor.fetchone()
    return query(fn, sql)

def all(sql):
    fn = lambda cursor: cursor.fetchall()
    return query(fn, sql)

def random(sql):
    fn = lambda cursor: cursor.fetchall()
    results = query(fn, sql)
    return get_random.choice(results)

def insert(sql):
    fn = lambda cursor: cursor.fetchall()
    return query(fn, sql)

def update(sql):
    fn = lambda cursor: cursor.fetchall()
    return query(fn, sql)
