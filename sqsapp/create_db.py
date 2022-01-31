import boto3
from . import config 

"""
sets up a table in dynamodb for storing the data from sqs consumed by the command tool
"""

def dbsetup():
    client = boto3.resource('dynamodb', endpoint_url=config.db_endpoint,
                      aws_access_key_id=config.aws_access_key_id,
                      aws_secret_access_key=config.aws_secret_access_key,
                      region_name=config.region_name)

    try:
        response = client.create_table(TableName=config.db_name,
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