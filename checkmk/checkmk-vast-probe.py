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
    print("VAST Alarms List")
    for alarm in client.alarms.get():
        print_api_response(alarm)

    # Print all SSDs
    print("VAST SSDs List")
    for ssd in client.ssds.get():
        print_api_response(ssd)

    # Print Cluster details and metrics
    print("VAST Cluster Details and Metrics")
    for cluster in client.clusters.get():
        print_api_response(cluster)



if __name__ == "__main__":
    main()
