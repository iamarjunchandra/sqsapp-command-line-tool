import boto3
import typer
from config import db_endpoint, db_name

"""
read, write and delete functions for the database
"""

def writetodb(id,msg):
    table = boto3.resource('dynamodb', endpoint_url=db_endpoint).Table(db_name)
    response=table.put_item(
        Item={
            'MessageID':id,
            'Message':msg
        }
    )

def readfromdb():
    try:
        table = boto3.resource('dynamodb', endpoint_url=db_endpoint).Table(db_name)
        response = table.scan()
        items = response['Items']
        while 'LastEvaluatedKey' in response:
            print(response['LastEvaluatedKey'])
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response['Items'])
        return items
    except:
        typer.echo(f"0 messages to retrieve; populate some messages using \"consume --count n queue url\" command")
        typer.Exit()


def clear():   
    client=boto3.client('dynamodb', endpoint_url=db_endpoint)
    try:
        response=client.delete_table(
            TableName=db_name
        )
    except:
        typer.echo(f"0 messages to clear; populate some messages using \"consume --count n queue url\" command")
        typer.Exit()
    
