import boto3


client=boto3.client('sqs',
                      endpoint_url="http://localhost:4566",
                      aws_access_key_id='test',
                      aws_secret_access_key='test')
for i in range(100):
    response = client.send_message(
        QueueUrl='http://localhost:4566/000000000000/test',
        MessageBody=f'{str(i)*3}'
    )
    print(f'{str(i)*3}')
