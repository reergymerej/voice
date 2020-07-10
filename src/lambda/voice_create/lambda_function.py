import json

def get_text(event):
    body = json.loads(event.get("body", "{}"))
    text = body.get('text')
    if not text:
        raise ValueError("no text found in request")
    return text

def lambda_handler(event, context):
    try:
        text = get_text(event)
        print('saving text: {}'.format(text))
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'text saved',
                'text': text,
            }),
            "headers": {
                "Access-Control-Allow-Origin":"*",
                "Content-Type": "application/json"
            },
        }
    except:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'missing "text" in request body',

            }),
            "headers": {
                "Access-Control-Allow-Origin":"*",
                "Content-Type": "application/json"
            },
        }

if __name__ == '__main__':
    event = None
    try:
        with open('./event.json') as f:
            event = json.load(f)
    except:
        print('running without event')
    result = lambda_handler(event, None)
    print(result)
