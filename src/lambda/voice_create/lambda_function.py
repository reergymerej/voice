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
        'command': 'add_feedback',
        'data': {
            'text': text,
        },
    })
    print('payload', payload)
    response = client.invoke(
        FunctionName='voice_db',
        Payload=payload,
    )
    parsed_response = json.loads(
        response['Payload'].read().decode()
    )
    try:
        return parsed_response['data']
    except KeyError as error:
        print(parsed_response['errorMessage'])
        print(''.join(parsed_response['stackTrace']))
        raise Exception('unable to save')

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
    try:
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
    except:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'problem saving',
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
