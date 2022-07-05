import boto3

client=boto3.client("ec2")

client.delete_vpc(
      VpcId='vpc-073afa99b9749b34a'
      
  )