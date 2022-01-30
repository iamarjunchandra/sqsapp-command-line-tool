from botocore.exceptions import ClientError
import logging
"""
fetch the attribute approximate number of messages in the queue
for validating the argument count of consume command to be less than the messages in queue
"""
logger = logging.getLogger(__name__)


def count_messages(client,url):
    try:
        response = client.get_queue_attributes(
            QueueUrl=url,
            AttributeNames=[
                'ApproximateNumberOfMessages'])
    except ClientError as error:
        logger.exception("Connection failed, Try again...")
        raise error
    else:
        return response['Attributes']['ApproximateNumberOfMessages']