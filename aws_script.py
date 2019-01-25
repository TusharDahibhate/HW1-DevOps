import boto3
import time

def initialize():
    """
        THIS FUNCTION INITIALIZES THE RESOURCE AND THE CLIENT
    """
    try:
        resource = boto3.resource('ec2')
        client = boto3.client('ec2')
        return resource, client
    except:
        print("ERROR: Could not initialize resource and client!")        

def print_regions(client):
    """
        THIS FUNCTION IS USED TO PRINT REGIONS
    """
    try:
        response = client.describe_regions()
    except:
        print("ERROR: Could not print the regions!")
    else:
        print("-----------------------")
        print("REGIONS:")
        print("-----------------------")
        for region in response['Regions']:
            print(region['RegionName'])    
        print("-----------------------")

def print_images(client):
    """
        THIS FUNCTION PRINTS IMAGES FOR THE REGION SPECIFIED IN THE CONFIG FILE
    """
    try:
        response = client.describe_images()
    except:
        print("ERROR: Could not print the images!")
    else:
        
        for image in response['Images']:
            print("-----------------------")
            print("IMAGES:")
            print("-----------------------")
            print("Image id: {} - {}".format(image['ImageId'], image['Platform']))
            print("-----------------------")

def create_instance(resource, configuration_options):
    """
        THIS FUNCTION CREATES AN INSTANCE
    """
    try:
        response = resource.create_instances(
                        ImageId = configuration_options['ImageId'],
                        MinCount = configuration_options['MinCount'],
                        MaxCount = configuration_options['MaxCount'],
                        InstanceType = configuration_options['InstanceType'],
                        KeyName = configuration_options['KeyName'],
                        SecurityGroups=configuration_options["SecurityGroups"])
    except:
        print("ERROR: Could not create an instance!")
    else:
        instance_id = response[0].instance_id
        print("SUCCESS: Instance created !")
        print("Instance Id: {}".format(instance_id))
        return response, instance_id

def print_instance_ip_address(resource, instance_id):
    """
        THIS FUNCTION PRINTS THE IP ADDRESS OF THE INSTANCE 
    """

    print(instance_id)
    print("Waiting..")    
    time.sleep(10)
    instances = resource.instances.filter(InstanceIds=[""+str(instance_id) + ""] )
    for instance in instances:
        print(instance.public_ip_address)        
    
if __name__ == "__main__":    

    ex2_resource, ec2_client = initialize()

    print_regions(ec2_client)    

    configuration_options = {
        ImageId : "ami-0ac019f4fcb7cb7e6",
        MinCount : 1,
        MaxCount : 1,
        InstanceType : "t2.micro",
        KeyName : "test_key",
        SecurityGroups : ['test']
    }

    response, instance_id = create_instance(ex2_resource, configuration_options)    

    print_instance_ip_address(ex2_resource, instance_id)
    