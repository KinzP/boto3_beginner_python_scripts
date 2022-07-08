import boto3

aws_region = "us-east-1"
tags = ['environment dev']
ec2 = boto3.resource('ec2')

ec2.instances.filter(InstanceTags = 'environment dev').stop( #for stopping an ec2 instance
    KeyName='LUIT_Project14', #input keypair name here
    Filters = 'environment dev',
    Values = 'environment dev' 
)

print("environment dev instance has been stopped")