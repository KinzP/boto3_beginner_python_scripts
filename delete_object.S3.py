import boto3
s3_resource=boto3.client("s3")

#delete single object
s3_resource.delete_object(Bucket='kparham-bucket-test-boto3',
      Key='canvas2.png')
      
#find all the objects from the bucket
objects=s3_resource.list_objects(Bucket="kparham-bucket-test-boto3")["Contents"]
len(objects)

#iteration
for object in objects:
    response=s3_resource.delete_object(Bucket='kparham-bucket-test-boto3',
      Key=object["Key"])
    print(response)