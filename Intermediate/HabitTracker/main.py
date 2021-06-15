import requests
import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "einoorish"
TOKEN = "sthg343fkhslfkm25sldkf"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# -- signup
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# creating graph
graph_config = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "Steps",
    "type": "int",
    "color": "shibafu"
}

auth_header = {
    "X-USER-TOKEN": TOKEN
}

# requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=auth_header)

# adding a pixel
POINT_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.date.today()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many steps did you do today?"),
}

# requests.post(url=POINT_ENDPOINT, json=pixel_config, headers=auth_header)

# updating a pixel

UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_config = {
    "quantity": "4117",
}

# requests.put(url=UPDATE_ENDPOINT, json=update_config, headers=auth_header)

# deleting a pixel

DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

requests.delete(url=DELETE_ENDPOINT, headers=auth_header)