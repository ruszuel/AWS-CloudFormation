import json
import boto3

def handler(event, context):
    print('api invoke')
    print(event)
    register_card(json.loads(event['body']))

    return {
        'statusCode': 200,
        'body': json.dumps('Card Successfully Registered')
    }


def register_card(item):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('card_account_cfn')
    item['status'] = 'INACTIVE'
    item['balance'] = 0
    table.put_item(
        Item=item    
    )