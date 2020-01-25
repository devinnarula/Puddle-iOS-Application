import requests
import os
from datetime import datetime, timedelta
geospaces = {}
access_token = "prj_test_sk_54ed50a4e9e77cde4b4708250e916a3ce27de10b"
def get_json(url,params):
    response = requests.get(
    url,
    params=params,
    headers={"Authorization": "{}".format(access_token)},
    )

    json_response = response.json()

    return json_response

def post_json(url,payload):
    post = requests.post(
    url,
    data=payload,
    headers={"Authorization": "{}".format(access_token)},
    )
    json_response = post.json()
    return json_response

def pull_geospace():
    return get_json('https://api.radar.io/v1/geofences',{})

def upload_polygon(parameters): #Parameters in [name,tag,coordinates] strings Coordinates in [[],[],...]
    current = datetime.now()
    name = parameters[0]
    tag = parameters[1]
    coordinates = parameters[2]
    payload = {'description' : name, 'type' : 'polygon', 'coordinates' : coordinates, 'tag' : tag, 'externalId' : current.strftime("%H%M%S")}
    post_json('https://api.radar.io/v1/geofences',payload)
    global geospaces
    geospaces = pull_geospace() 
upload_polygon(['Test','ICE','[[34.68216965456513, -82.84807573583319],[34.68140454618486, -82.8367726354168],[34.67935767062538, -82.83029241843673],[34.67381673639116, -82.83140821738792],[34.68216965456513, -82.84807573583319]]'])
print(geospaces)