# voice_db

This is the only lambda that will interact with the database.  This allows other
routes to call it without spreading db logic and auth everywhere.

`psycopg2/` is in the package.zip, but not included locally.  This is because
locally, use the one from Pipenv.  In Lambda, use the one in the zip.

## Integration

Other functions can call this one if they have the proper permissions
(lambda:InvokeFunction).  This is done through boto3.

```
client = boto3.client('lambda')
payload = json.dumps({
    'command': 'some_sweet_command',
    'data': {
        'text': 'whatever',
        'you': 'want',
    },
})
client.invoke(
    FunctionName='voice_db',
    Payload=payload,
)
```
`command` tells the db module what you want to run.
`data` is open-ended JSON and varies per command.
