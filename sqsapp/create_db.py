import boto3
from config import db_endpoint,db_name

"""
sets up a table in dynamodb for storing the data from sqs consumed by the command tool
"""

def dbsetup():
    client = boto3.resource('dynamodb', endpoint_url=db_endpoint)

    try:
        response = client.create_table(TableName=db_name,
            AttributeDefinitions=[
                {
                    'AttributeName': 'MessageID',
                    'AttributeType': 'S',
                },
                {
                    'AttributeName': 'Message',
                    'AttributeType': 'S',
                },
            ],
            KeySchema=[
                {
                    'AttributeName': 'MessageID',
                    'KeyType': 'HASH',
                },
                {
                    'AttributeName': 'Message',
                    'KeyType': 'RANGE',
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5,
            },
        )
    except:
        pass

if __name__=="__main__":
    dbsetup()