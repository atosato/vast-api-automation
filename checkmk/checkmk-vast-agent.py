import json
import os
from dotenv import load_dotenv, find_dotenv
from vastpy import VASTClient


output_filename = "vast_data_api.out"

#Initialize the output file
def init_output_file():
    print(f"Create an empty new: {output_filename}\n")
    file = open(output_filename, "w") # Append to file
    file.close()

#Print API response to file (and to screen)
def print_to_file(text_to_write):
    print(f"{text_to_write}\n")
    file = open(output_filename, "a") # Append to file
    file.write(f"{text_to_write}\n")
    file.close()

#Print raw API response for debug purpose
def print_api_response(api_response):
    print("------------------------------------------------------------------------------------")
    print(api_response)
    for key, value in api_response.items():
        print(key, value)


############# MAIN ##############
def main():
    #load_dotenv(find_dotenv())  # Load the .env file.
    load_dotenv()  # Load the .env file.
    # Fetch variables from the .env file.
    API_USERNAME = os.getenv("API_USERNAME")
    API_PASSWORD = os.getenv("API_PASSWORD")
    VMS_IP = os.getenv("VMS_IP")

    client = VASTClient(user=API_USERNAME, password=API_PASSWORD, address=VMS_IP)
    init_output_file()

    # Print all Alarms
    print_to_file("<<<vast_data_alarms:sep(0)>>>")
    for alarm in client.alarms.get():
        print_to_file(json.dumps(alarm))
        #print_api_response(alarm)

    # Print Cluster details and metrics
    print_to_file("<<<vast_data_cluster:sep(0)>>>")
    for cluster in client.clusters.get():
        print_to_file(json.dumps(cluster))
        #print_api_response(cluster)

    # Print all SSDs
    print_to_file("<<<vast_data_ssds:sep(0)>>>")
    for ssd in client.ssds.get():
        print_to_file(json.dumps(ssd))
        #print_api_response(ssd)

    print_to_file("<<<vast_data_tenants:sep(0)>>>")
    for tenant in client.tenants.get():
        print_to_file(json.dumps(tenant))
        #print_api_response(tenant)

    print_to_file("<<<vast_data_views:sep(0)>>>")
    for view in client.views.get():
        print_to_file(json.dumps(view))
        #print_api_response(view)




if __name__ == "__main__":
    main()
