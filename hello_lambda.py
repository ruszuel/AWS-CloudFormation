
def handler(event, context):
    print("api invoke")
    return {
        "statusCode": 200,
        "body": "Hello from Lambda"
    }