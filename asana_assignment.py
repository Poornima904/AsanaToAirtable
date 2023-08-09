import asana
from asana.rest import ApiException
from pprint import pprint
import requests
from pyairtable import Api
import datetime
import string
import random
import os
import time
import json

# Write a list to a file
def write_list_to_file(file_path, input_list):
    with open(file_path, 'w') as file:
        for item in input_list:
            file.write(str(item) + '\n')

# Read the list from a file
def read_list_from_file(file_path):
    output_list = []
    with open(file_path, 'r') as file:
        for line in file:
            output_list.append(line.strip())
    return output_list


def create_file_if_not_exists(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("[]")

api = Api('patz2tyErOQEDyTw2.dea10652825763e297ba4289ae6787b6e33604e780f72dace7089429ead806a3')
table = api.table('appA0NM7UDuYuhK3D', 'Asana Tasks')

print("Starting now...........")
print("Press CTRL+Z to quit.....")
while True:

    time.sleep(10)

    import requests

    url = "https://app.asana.com/api/1.0/tasks?project=1205240723217588"

    headers = {
        "accept": "application/json",
        "authorization": "Bearer 1/1205223399173260:7e3c6743a9640fed6eeb21e4060b6ac3"
    }

    response = requests.get(url, headers=headers)

    try:
        create_file_if_not_exists('my_list.txt')
        # Read the list from the file
        read_list = read_list_from_file('my_list.txt')
        # Get multiple tasks
        api_response = response.json()
        for api_resp in api_response['data']:
            id = api_resp['gid']
            name = api_resp['name']
            due_date = 'N/A'
            try:
                description = api_resp['resource_subtype']
            except:
                description = "N/A"
            
            try:
                assignee = api_resp['assignee'].get('name', 'N/A')
            except:
                assignee = "N/A"

            if id not in read_list:
                read_list.append(id)
                response = table.create({
                    "TaskId": id,
                    "Name": name,
                    "Assignee": assignee,
                    "Due Date": due_date,
                    "Description": description
                    })
        # Write the list to a file
        write_list_to_file('my_list.txt', read_list)

    except ApiException as e:
        print("Exception when calling TasksApi->get_tasks: %s\n" % e)