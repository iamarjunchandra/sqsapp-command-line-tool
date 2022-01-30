import boto3


client=boto3.client('sqs',
                      endpoint_url="http://localhost:4566",
                      aws_access_key_id='test',
                      aws_secret_access_key='test')

response = client.get_queue_attributes(
    QueueUrl='http://localhost:4566/000000000000/test',
    AttributeNames=[
        'ApproximateNumberOfMessages']
)
print(response['Attributes']['ApproximateNumberOfMessages'])