import db
import json
import os

def do_query(user_id):
    query = """
        select '{user_id}'
    """.format(
        user_id = user_id,
    )
    print(query)
    if os.getenv('DEV'):
        print("skipping db")
        return
    return db.all(query)

def sanity():
    result = do_query('sanity acheived')
    return json.dumps(result)

def lambda_handler(event, context):
    print('event', event)
    result = sanity()
    return result

if __name__ == '__main__':
    event = None
    try:
        with open('./event.json') as f:
            event = json.load(f)
    except:
        print('running without event')
    result = lambda_handler(event, None)
    print(result)
