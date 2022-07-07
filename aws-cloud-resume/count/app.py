import boto3
import json

# define dynamoDB resource and table
table = boto3.resource('dynamodb').Table('cloud-resume-challenge')

def lambda_handler(event, context):
    # get visitorCount from dynamoDB and iterate by 1
    response = table.get_item(Key={'id':'1'})
    count =  response['Item']['visitorCount'] + 1
    # update visitorCount in dynamoDB
    table.update_item(
        Key={'id':'1'},
        AttributeUpdates={
            'visitorCount': {"Value": count},
        },
    )
    # return visitorCount
    message = {
   'message': str(count)
    }
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,GET'
        },
        'body': json.dumps(message)
    }
