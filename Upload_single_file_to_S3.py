import boto3

#how to upload single file
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="Test_upload_file.txt",
    Bucket="kparham-bucket-test-boto3",
    Key="Test_upload_file.txt")