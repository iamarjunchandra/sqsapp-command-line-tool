import boto3


client=boto3.client('sqs',
                      endpoint_url="http://localhost:4566",
                      aws_access_key_id='test',
                      aws_secret_access_key='test')

response = client.receive_message(
    QueueUrl='http://localhost:4566/000000000000/test',
    MaxNumberOfMessages=10
)
# print messages
receipt_handler=[]
for msg in response['Messages']:
   print(f'ID: {msg["MessageId"]}, Message: {msg["Body"]}')
   receipt_handler.append(msg['ReceiptHandle'])

#delete read messages
for receipt in receipt_handler:
    response = client.delete_message(
        QueueUrl='http://localhost:4566/000000000000/test',
        ReceiptHandle=receipt
    )
