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
1. The script is written in Python3.
2. The script depends on boto3.
3. The requirements.txt file contains all the dependencies required for the script to run. 
4. To resolve the dependencies, run 
 ```bash
 $ pip install -r requirements.txt 
```
### Configuration Options:
You can configure the stript to create the instance that you desire.

Following are the configuration options that can be set:
1. ImageId - This specifies what base image that you want for your instance. Example - Ubuntu, RedHat, etc.
2. MinCount - The minimum number of instances that you would like to spawn.
3. MaxCount - The maximum number of instances that you would like to spawn.
4. InstanceType - It specifies the hardware configuration of the instance. Free Tier only provides t2.micro.(More information here: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
5. KeyName - The SSH key that will be used to SSH into the instance that you will create.
6. SecurityGroups - The security groups will control the access to the instance that you will create.\

Region can be specified here but in this script, region will be taken from the config file.(More information here: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html) 

### Executing the script:
1. To execute the script use the following command
```bash
$ python aws_script.py
```
2. The script will execute and the instance will be created. The IP address of the instance will be displayed.

### Accessing the instance:
1. You can use the IP address to ssh into the instance that was just spawned.
```bash
$ ssh -i [location]/test_key.pem ubuntu@[IP address]
```
### Resources:
1. https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
2. https://aws.amazon.com/sdk-for-python/

# Google Cloud Platform
1. gcp_script.py contains the code for automatic provisioning of an Google cloud compute resource.
2. The script uses Python Client Library for Compute Engine API. 

### Manual Steps:
1. Create a google cloud account by navigating here : https://cloud.google.com/
2. Create a project by navigating to Getting Started -> Create an empty project
3. After the project is created, go to the project dashboard.
4. Navigate to API & Services -> Create Credentials -> Service Account Key
5. Create a Service account key and assign the role of owner.
6. A private key will be downloaded which will be used to access the resources on the cloud platform. This key will be in the form of a json file.
7. Set an environment variable in the following manner 
```bash
$ export GOOGLE_APPLICATION_CREDENTIALS =”[PATH]/[FILE_NAME].json”
```
8. Go to the SSH keys tab in the Metadata section of the Compute Engine dashboard. 
9. If you have an SSH key generated, go to .ssh folder in your home directory and open the file id_rsa.pub. This is your public SSH key that you can use to access the compute instance.
10. If you don’t have an SSH key, generate one using the following command
```bash
$ ssh-keygen -t rsa
```
11. Copy and paste your SSH key in the text box given and save. 
12. This will give you project wide access to any resource using your SSH key. 
13. Google Python Client Library for Google Compute Engine will use the credentials set in step 7 to authenticate the user every time an API call is made to create an instance.

### Dependencies:
1. The script was written in Python3
2. It has a dependency on Python Client Library for Compute Engine API.
3. The requirements.txt file contains all the dependencies required for the script to run. 
4. To resolve the dependencies, run 
 ```bash
 $ pip install -r requirements.txt 
```

### Configuration options:
In this script, you can configure the instance as per your requirement.
Following are the configuration options present.
1. project_id - Specifies under what project the instance will be spawned
2. image_project - Specifies different image projects (More details in the Images section of the Compute Engine Dashboard)
3. image_family - Specifies the image family (More details in the Images section of the Compute Engine Dashboard)
4. zone_name - Specifies the zone (More details in the Zones section of the Compute Engine Dashboard)
5. machine_type - Specifies the machine type (More information here: https://cloud.google.com/compute/docs/machine-types)
6. instance_name - This is the instance identifier

### Executing the script:
1. To execute the script use the following command
```bash
$ python gcp_script.py
```
2. The script will execute and the instance will be created. The IP address of the instance will be displayed.

### Accessing the instance:
1. You can use the IP address to ssh into the instance that was just spawned.
```bash
$ ssh [IP address]
```
### Resources:
1. https://cloud.google.com/compute/docs/reference/rest/v1/
2. https://cloud.google.com/compute/docs/tutorials/python-guide#before-you-begin
