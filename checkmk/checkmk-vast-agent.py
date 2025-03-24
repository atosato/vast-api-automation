import json
import os
from dotenv import load_dotenv, find_dotenv
from vastpy import VASTClient

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

    # Print all Alarms
    print("<<<vast_data_alarms:sep(0)>>>")
    for alarm in client.alarms.get():
        print(alarm)
        #print_api_response(alarm)

    # Print Cluster details and metrics
    print("<<<vast_data_cluster:sep(0)>>>")
    for cluster in client.clusters.get():
        print(cluster)
        #print_api_response(cluster)

    # Print all SSDs
    print("<<<vast_data_ssds:sep(0)>>>")
    for ssd in client.ssds.get():
        print(ssd)
        #print_api_response(ssd)

    print("<<<vast_data_tenants:sep(0)>>>")
    for tenant in client.tenants.get():
        print(tenant)
        #print_api_response(tenant)

    print("<<<vast_data_views:sep(0)>>>")
    for view in client.views.get():
        print(view)
        #print_api_response(view)




if __name__ == "__main__":
    main()
