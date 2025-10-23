import json
def handler(event, context):
    print("api invoke")
    print("#event")
    print(json.dumps(event, indent=2))
    name = event.get("queryStringParameters").get("name", "")

    return {
        "statusCode": 200,
        "body": f"Hello {name} from lambda"
    }

    # return f"Hello {name} from lambda"