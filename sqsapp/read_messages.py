import boto3
from botocore.exceptions import ClientError
from config import endpoint_url
from . import count_message
import logging
import typer

logger = logging.getLogger(__name__)

"""
Reads the message from SQS queue and stroes in dynamodb-local table called 'sqsapp-db'
"""

def read_message(n,url):
    client=boto3.client('sqs',
                      endpoint_url=endpoint_url)
    query_len=int(count_message.count_messages(client,url))
    if query_len>=n:
        query_data=[]
        for i in range(n):
            try:
                response = client.receive_message(
                    QueueUrl=url,
                    MaxNumberOfMessages=1,
                    VisibilityTimeout=300,
                    WaitTimeSeconds=20
                )
                
                for msg in response['Messages']:
                    query_data.append([msg["MessageId"],msg["Body"]])
                    #delete the processed message from SQS
                    try:
                        response = client.delete_message(
                        QueueUrl=url,
                        ReceiptHandle=msg['ReceiptHandle']
                        )
                    except:
                        pass
            except ClientError as error:
                logger.exception("Connection failed")
                raise error
        return query_data

    else:
        typer.echo(f"Count argument is greater than the messages in queue, queue size = {query_len}. Try Again with a lower value..")
        raise typer.Exit()
