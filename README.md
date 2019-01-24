# CSC 519- DevOps Homework 1 - Provisioning Servers

### Student Name: Tushar Himmat Dahibhate
### Unity Id: tdahibh

This file will describe the deliverables for Homework 1.

For this homework, I have selected Amazon Web Services and Google Cloud Platform as the cloud providers.
The following sections will describe in detail, what all things were done to automate the provisioning.

# Amazon Web Services

1. aws_script.py contains the code for automatic provisioning of an AWS Elastic Cloud Compute(EC2) resource. 
2. The script uses Boto3 module which is the AWS SDK for python. 

### Manual steps:
1. Create a free tier account at https://aws.amazon.com/
2. Login and navigate to the Management console.
3. Go to IAM dashboard and create a user.
4. Assign Administrator privileges to the user. 
5. You will then get security credentials for the user that you created.
6. Create a folder named .aws in the home directory of your machine to store the credentials.
7. In the .aws directory, create 2 files named config and credentials.
8. Copy the credentials you received in step 5 inside the credentials file in the following manner.

```bash
  [default]
  aws_access_key_id = [Your access id]
  aws_secret_access_key = [Your access key]
```
9. In the config file you can past some configuration options like the region.
```bash
  [default]
  region=us-east-1
```
10. Go to the EC2 dashboard and create a security group. The security group will specify what all IP addresses can access the EC2 instance.
11. Go to the EC2 dashboard and create a key pair. This key will be used to ssh into the instance that you will be creating.  Download the key and change its permission.
```bash
  $ chmod 400 key_name.pem
```

### Dependencies:
1. The script depends on boto3.
2. The requirements.txt file contains all the dependencies required for the script to run. 
3. To resolve the dependencies, run 
 ```bash
 pip install -r requirements.txt 
```

### Executing the script:
1. To execute the script use the following command
```bash
python aws_script.py
```
2. The script will execute and the instance will be created. The IP address of the instance will be displayed.

### Accessing the instance:
1. You can use the IP address to ssh into the instance that was just spawned.
```bash
ssh -i [location]/test_key.pem ubuntu@[IP address]
```




	

 






 




## Google Cloud Platform

