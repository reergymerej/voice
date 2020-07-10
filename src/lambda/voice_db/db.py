import random as get_random
from connect import get_connection
import psycopg2
from psycopg2.extras import RealDictCursor
import os

def query(fn, sql, data):
    print("query:", sql)
    if os.getenv('DEV'):
        print("skipping db")
        return
    connection = get_connection()
    cursor = connection.cursor(None, cursor_factory=RealDictCursor)
    # cursor.execute("query with params %s %s", ("param1", "pa'ram2"))
    cursor.execute(sql, data)
    if fn:
        result = fn(cursor)
    connection.commit()
    connection.close()
    cursor.close()
    return result

def one(sql, data):
    fn = lambda cursor: cursor.fetchone()
    return query(fn, sql, data)

def all(sql, data):
    fn = lambda cursor: cursor.fetchall()
    return query(fn, sql, data)

def random(sql, data):
    fn = lambda cursor: cursor.fetchall()
    results = query(fn, sql, data)
    return get_random.choice(results)

def insert(sql, data):
    fn = lambda cursor: cursor.fetchall()
    return query(fn, sql, data)

def update(sql, data):
    fn = lambda cursor: cursor.fetchall()
    return query(fn, sql, data)
