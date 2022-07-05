#how to upload multiple files to S3 bucket
import os
import glob
import boto3

objects=s3_resource(Bucket="kparham-bucket-test-boto3")


s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="Test_file.txt""KParhamtest.txt" ,
    (Bucket="kparham-bucket-test-boto3"),
    Key=file.split("Test_file.txt"/"KParhamtest.txt")[-1])