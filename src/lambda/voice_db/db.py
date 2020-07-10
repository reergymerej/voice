import random as get_random
from connect import get_connection
from psycopg2.extras import RealDictCursor

def query(fn, sql):
    try:
        connection = get_connection()
        cursor = connection.cursor(None, cursor_factory=RealDictCursor)
        cursor.execute(sql)
        if fn:
            result = fn(cursor)
        connection.commit()
        connection.close()
        cursor.close()
        return result
    except:
        print('unable to perform query')

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
