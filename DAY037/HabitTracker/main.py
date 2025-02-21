import requests
from datetime import datetime
pixela_endpoint="https://pixe.la/v1/users"
TOKEN="suibwejhfbgsjgsufjsfni"
USERNAME="arif2410"
GRAPH_ID = "graph-running"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsofService":"yes",
    "notMinor":"yes",
}

# create a user in pixela
#response=requests.post(url=pixela_endpoint,json=user_params)
#print(response.text)


graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id": GRAPH_ID,
    "name":"running",
    "unit":"Km",
    "type":"float",
    "color":"sora"
}
# You can attach your API key to a request in one ofthree ways:
# - Via the API Key querystring parameter
# - Via X-API-KEY HTTP header
# - Via the Authorization HTTP header
# Option 2 and 3 are more secure

headers={
    "X-USER-TOKEN":TOKEN
}

# Create a graph
# response = requests.post(url=f"{pixela_url}/{USERNAME}/graphs", json=graph_config, headers=headers)
# print(response.text)
# view graph at: https://pixe.la/v1/users/USERNAME/graphs/graph_id.html

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)


pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today=datetime.now()
today1=datetime(year=2024,month=12,day=2)
#print(today.strftime("%Y%m%d"))
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many Kilometers did you run")
}
response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today1.strftime('%Y%m%d')}"

new_pixel_data={
    "quantity":"4.0"
}
# response=requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today1.strftime('%Y%m%d')}"
#response=requests.delete(url=delete_endpoint,headers=headers)
#print(response.text)
