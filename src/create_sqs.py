import boto3


client=boto3.client('sqs',
                      endpoint_url="http://localhost:4566",
                      aws_access_key_id='test',
                      aws_secret_access_key='test')

response = client.create_queue(QueueName='test')

response = client.list_queues()

for url in response['QueueUrls']:
    print(url)
