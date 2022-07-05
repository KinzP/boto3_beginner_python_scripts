# create a S3 Buckets

import boto3

client = boto3.client("s3")


client.create_bucket(Bucket="kparham-bucket-test-boto3") 