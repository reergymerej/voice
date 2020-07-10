import json
import boto3

def get_text(event):
    body = json.loads(event.get("body", "{}"))
    text = body.get('text')
    if not text:
        raise ValueError("no text found in request")
    return text

def save(text):
    client = boto3.client('lambda')
    payload = json.dumps({
        'command': 'sanity',
        'data': {
            'text': text,
        },
    })
    print('payload', payload)
    response = client.invoke(
        FunctionName='voice_db',
        InvocationType='Event',
        Payload=payload,
    )
    print('response from save', response)
    return response

def lambda_handler(event, context):
    text = None
    try:
        text = get_text(event)
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

    print('saving text: {}'.format(text))
    result = save(text)
    print('result', result)
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


if __name__ == '__main__':
    event = None
    try:
        with open('./event.json') as f:
            event = json.load(f)
    except:
        print('running without event')
    result = lambda_handler(event, None)
    print(result)
