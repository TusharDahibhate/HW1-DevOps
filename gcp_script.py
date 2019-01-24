import googleapiclient.discovery
import time

def initialize():
    """
        THIS FUNCTION WILL BUILD AN OBJECT TO ACCESS THE COMPUTE RESOURCE USING V1 COMPUTE ENGINE API
    """

    try:
        compute = googleapiclient.discovery.build('compute', 'v1')
    except:
        print("ERROR: Could not Initialize!")
    else:
        return compute

def print_images(image_project):
    """
        THIS FUNCTION WILL PRINT A LIST OF ALL THE PUBLICLY IMAGES AVAILABLE FOR A GIVEN IMAGE PROJECT
    """

    try:
        images = compute.images().list(project = image_project).execute()
    except:
        print("ERROR: Could not fetch the images!")
    else:
        print("---------------------- AVAILABLE IMAGES ---------------------------")    
        for image in images['items']:
            print("Image Id: {} --> Name: {}".format(image['id'], image['name']))
        print("-------------------------------------------------------------------")

def print_regions(project_id):
    """
        THIS FUNCTION WILL PRINT A LIST OF ALL THE REGIONS FOR A GIVEN IMAGE PROJECT ID
    """

    try:
        regions = compute.regions().list(project = project_id).execute()
    except:
        print("ERROR: Could not fetch the regions!")
    else:
        print("------------------------- REGIONS ---------------------------------")
        for region in regions['items']:
            print("Id: {} --> Name: {}".format(region['id'], region['name']))
        print("-------------------------------------------------------------------")

def print_zones(project_id):
    """
        THIS FUNCTION WILL PRINT A LIST OF ALL THE ZONES FOR A GIVEN IMAGE PROJECT ID
    """

    try:
        zones = compute.zones().list(project = project_id).execute()
    except:
        print("ERROR: Could not fetch the zones!")
    else:
        print("------------------------- ZONES -----------------------------------")
        for zone in zones["items"]:
            print("Id: {} --> Name: {}".format(zone['id'], zone['name']))
        print("-------------------------------------------------------------------")


def construct_machine_type_url(zone_name, machine_type):
    """
        THIS FUNCTION WILL CONSTRUCT THE URL FOR THE MACHINE TYPE PROPERTY 
    """

    url = 'zones/' + zone_name + '/machineTypes/' + machine_type
    return url

def get_image_data(image_project, image_family):
    """
        THIS FUNCTION RETURNS THE IMAGE DATA FOR THE GIVEN IMAGE FAMILY AND IMAGE PROJECT
    """
    try:
        image_data = compute.images().getFromFamily(project = image_project, family = image_family).execute()
    except:
        print("ERROR: Could not fetch the image data!")
    else:
        return image_data

def create_instance(machine_type_url, image_data, zone_name, project_id, instance_name):
    body = {
    'name' : instance_name,
    'machineType' : machine_type_url,
    'networkInterfaces': [{
        'network': 'global/networks/default',
        'accessConfigs': [
            {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
        ]
    }],
    'disks': [
       {
            'boot': True,
            'autoDelete': True,
            'initializeParams': {
                'sourceImage': image_data['selfLink'],
            }
        }
        ],
    }
    try:
        response = compute.instances().insert(project = project_id, zone = zone_name, body = body).execute()
    except:
        print("ERROR: Could not create the instance!")
    else:
        return response

def get_instance_details(project_id, zone_name, instance_name):
    """
        THIS FUNCTION RETURNS THE INSTANCE DETAILS
    """
    try:
        response = compute.instances().get(project = project_id, zone = zone_name, instance = instance_name).execute()    
    except:
        print("ERROR: Could not fetch the instance details!")
    else:            
        return response

if __name__ == "__main__":

    project_id = 'calm-library-229319'
    image_project = 'gce-uefi-images'
    image_family = 'ubuntu-1804-lts'
    zone_name = 'us-east1-b'
    machine_type = 'n1-standard-1'
    instance_name = 'devops-v6'

    compute = initialize()
    print_images(image_project)
    print_regions(project_id)
    print_zones(project_id)

    image_data = get_image_data(image_project, image_family)

    machine_type_url = construct_machine_type_url(zone_name, machine_type)

    creation_response = create_instance(machine_type_url, image_data, zone_name, project_id, instance_name)

    print(creation_response)
    time.sleep(10)

    instance_details = get_instance_details(project_id, zone_name, instance_name)
    
    print(instance_details['networkInterfaces'][0]['accessConfigs'][0]['natIP'])