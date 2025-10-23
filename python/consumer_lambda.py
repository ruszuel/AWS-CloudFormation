import json

def handler(event, context):
    print("event received")
    print(json.dumps(event, indent=2))

    return "ok"