#!/usr/bin/env python3.9
import boto3

ec2 = boto3.resource('ec2')
no_of_instances = int(input("How many instances:" ))

instance = ec2.create_instances(
    ImageId="ami-0cff7528ff583bf9a", #input AMI here
    InstanceType='t2.micro',
    KeyName='LUIT_Project14', #input keypair name here
    MaxCount= 3,
    MinCount= 3
)
print(instance)