import os

import boto3


class S3Client:
    def __init__(self):
        self.queue = os.getenv('AWS_QUEUE_URL')
        self.client = boto3.client(
            service_name='sqs',
            endpoint_url=self.queue,
            region_name=os.getenv('S3_REGION'),
            aws_access_key_id=os.getenv('S3_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('S3_SECRET_ACCESS_KEY')
        )

    def get_messages_from_queue(self, count=10):
        return self.client.receive_message(
            QueueUrl=self.queue,
            MaxNumberOfMessages=count,
            VisibilityTimeout=60,
            WaitTimeSeconds=20
        ).get('Messages')

    def delete_message_from_queue(self, message):
        self.client.delete_message(
            QueueUrl=self.queue,
            ReceiptHandle=message.get('ReceiptHandle')
        )