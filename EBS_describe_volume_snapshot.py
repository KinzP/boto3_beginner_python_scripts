#describe aws ebs volume snapshot using boto3 and python

import boto3
ec2_boto3=boto3.client("ec2")

ec2_boto3.describe_snapshots(SnapshotIds=[
          'snap-03f0a437fd2dea30e'
      ])