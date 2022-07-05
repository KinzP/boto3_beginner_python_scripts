import boto3
client=boto3.client("ec2")

#describe all vpc is available in your account
x=client.describe_vpcs()

no_of_vpcs=x["Vpcs"]

len(no_of_vpcs)

for vpc in no_of_vpcs:
    print(vpc["VpcId"])
    

#describe one vpc based on vpc id
x=client.describe_vpcs(VpcIds=["vpc-0ef6da8498043a9a5","vpc-0562ba7c1845b54a4"])

# describe vpc based on filter

x=client.describe_vpcs()
x=client.describe_vpcs(Filters=[
          {
              'Name': 'vpc-id',
              'Values': [
                  'vpc-0ef6da8498043a9a5',
                  'vpc-0562ba7c1845b54a4'
                  
              ]
          },
      ])