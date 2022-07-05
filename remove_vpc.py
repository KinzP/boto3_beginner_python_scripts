import boto3

client=boto3.client("ec2")

response = client.delete_vpc(
      VpcId='vpc-073afa99b9749b34a'
      
  )