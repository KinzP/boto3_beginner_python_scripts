import boto3

#Search s3 bucket names on AWS

resource=boto3.resource( "s3" )

bucket_list=list(resource.buckets.all())

len(bucket_list)

for bucket in resource.buckets.all():
    print(bucket.name)