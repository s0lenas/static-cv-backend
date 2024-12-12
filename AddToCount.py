import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitors')

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={
                "value_id" : 0
            },
            UpdateExpression="SET #c = #c + :val",
            ExpressionAttributeValues={
                ':val': 1
            },
            ExpressionAttributeNames={
                "#c": "count"
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
    except:
        raise