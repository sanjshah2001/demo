import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-9afbd6ff',
    SubnetId='subnet-4537fc08',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')
