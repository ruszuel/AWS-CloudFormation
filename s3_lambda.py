import json

def handler(event, context):
    print("s3 event")
    print(json.dumps(event, indent=2))

    return "ok"