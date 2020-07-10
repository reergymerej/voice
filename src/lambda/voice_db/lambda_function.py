import db
import json

def sanity(anything):
    query = "select '{0}'".format(anything)
    result = db.all(query)
    return json.dumps(result)

def add_feedback(feedback):
    query = """
        INSERT INTO feedback (text)
        VALUES ('{feedback}')
        RETURNING *
    """.format(feedback=feedback)
    result = db.insert(query)
    return json.dumps(result)

def lambda_handler(event, context):
    print('EVENT', event)
    command = event.get('command')
    data = event.get('data')
    result = {
        'data': None,
        'message': None,
        'success': True,
    }

    if command == 'sanity':
        result['data'] = sanity(json.dumps(data))
    elif command == 'add_feedback':
        result['data'] = add_feedback(data['text'])
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
