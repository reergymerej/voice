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
    print('EVENT', event)
    command = event.get('command')
    result = {
        'data': None,
        'message': None,
        'success': True,
    }

    if command == 'sanity':
        result['data'] = sanity()
    else:
        result['success'] = False
        result['message'] = 'no command specified'

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
