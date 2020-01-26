import requests
from datetime import datetime
import os
import json
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
def clean_geo(rawcode):
    data={}
    data['instances']=[]
    # for i in range(0,len(rawcode['geofences'])):
    #     data['instances'].append({'Description':rawcode['geofences'][i]['description'],'Tag':rawcode['geofences'][i]['tag'],'externalId':rawcode['geofences'][i]['externalId'],'Coordinates':rawcode['geofences'][i]['geometry']['coordinates'][0]})
    for i in range(0,len(rawcode['geofences'])):
        data['instances'].append({'Coordinates':rawcode['geofences'][i]['geometryCenter']['coordinates']})
    return data
def pull_geospace():
    return get_json('https://api.radar.io/v1/geofences',{})
def upload_polygon(parameters): #Parameters in [name,tag,coordinates] strings Coordinates in [[],[],...]
    current = datetime.now()
    name = parameters['name']
    tag = parameters['tag']
    coordinates = parameters['coordinates']
    payload = {'description' : name, 'type' : 'circle', 'coordinates' : coordinates, 'radius' : 50, 'tag' : tag, 'externalId' : current.strftime("%d%H%M%S")}
    global geospaces
    geospaces = pull_geospace() #send geospaces back to client after this
    return post_json('https://api.radar.io/v1/geofences',payload)
# print(upload_polygon({'name' : 'nope', 'tag' : 'geat', 'coordinates' : [-82.84807573583119, 34.68216965456513]}))
# print(clean_geo(pull_geospace()))
