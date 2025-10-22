import json
import boto3
import os

def handler(event, context):
    print("# event received")
    print(json.dumps(event, indent=2))
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    object_key = event["Records"][0]["s3"]["object"]["key"]
    message = f"A file hase been uploaded to {bucket_name} \n File name: {object_key}"

    sqs = boto3.client('sqs')
    queue_url = os.getenv("queue_url", None)
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )
    print(message)
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
