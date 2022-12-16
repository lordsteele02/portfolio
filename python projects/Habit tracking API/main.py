import requests
from datetime import datetime

USERNAME = "steele434343"
TOKEN = "hg43hg43hg43hg"
GRAPH_ID = "graph1"


"""register with website"""
pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=parameters)
#print(response.text)



"""create a graph"""
#graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)


"""add a pixel to graph"""
add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many kilometers did you cycle today? ")
}

response = requests.post(url=add_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)


"""Update a pixel from before dates"""
#today = datetime(year=2022, month=4, day=22)
#update_date_data = today.strftime("%Y%m%d")
#update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{update_date_data}"

#update_pixel_config = {
#    "quantity": "5.4"
#}

#response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
#print(response.text)



"""Delete a pixel from the graph"""
#today = datetime(year=2022, month=4, day=22)
#delete_date_data = today.strftime("%Y%m%d")
#delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date_data}"
#
#response = requests.delete(url=delete_pixel_endpoint, headers=headers)
#print(response.text)
