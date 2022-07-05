import boto3
s3_resource=boto3.client("s3")

#delete single object
s3_resource.delete_object(Bucket='kparham-bucket-test-boto3',
      Key='canvas2.png')