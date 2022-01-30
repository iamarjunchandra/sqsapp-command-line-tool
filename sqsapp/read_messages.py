import boto3
from botocore.exceptions import ClientError
import config
from . import count_message

def read_message(n,url):
    client=boto3.client('sqs',
                      endpoint_url=config.endpoint_url)
    try:
        if count_message.count_messages(client,url)>n:
            response = client.receive_message(
                QueueUrl=url,
                AttributeNames=[
                'ApproximateNumberOfMessages'],
                MaxNumberOfMessages=1,
                VisibilityTimeout=300,
                WaitTimeSeconds=20
            )

        # print messages
        query_data=[]
        for msg in response['Messages']:
            query_data.append([msg['ReceiptHandle'],msg["MessageId"],msg["Body"]])
        return query_data

