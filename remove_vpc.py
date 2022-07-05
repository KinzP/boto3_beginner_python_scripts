import boto3

client=boto3.client("ec2")

response = client.delete_vpc(
      VpcId='vpc-0ef6da8498043a9a5'
      
  )