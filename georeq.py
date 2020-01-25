import requests
import os
from datetime import datetime, timedelta
import json
import boto3
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
    for i in range(0,len(rawcode['geofences'])):
        data['instances'].append({'Description':rawcode['geofences'][i]['description'],'Tag':rawcode['geofences'][i]['tag'],'externalId':rawcode['geofences'][i]['externalId'],'Coordinates':rawcode['geofences'][i]['geometry']['coordinates'][0]})
    return data
def pull_geospace():
    return get_json('https://api.radar.io/v1/geofences',{})
def upload_polygon(parameters): #Parameters in [name,tag,coordinates] strings Coordinates in [[],[],...]
    current = datetime.now()
    name = parameters[0]
    tag = parameters[1]
    coordinates = str(parameters[2])
    payload = {'description' : name, 'type' : 'polygon', 'coordinates' : coordinates, 'tag' : tag, 'externalId' : current.strftime("%H%M%S")}
    server_output = str(post_json('https://api.radar.io/v1/geofences',payload))
    s3 = boto3.resource('s3')
    s3.Object('puddlebucket', 'newfile.txt').put(Body=server_output)
    global geospaces
    geospaces = pull_geospace() #send geospaces back to client after this
upload_polygon(['nope','geat',[[-82.84807573583119, 34.68216965456513], [-82.8367726354168, 34.68140454618486], [-82.83029241843683, 34.67935767062518], [-82.83140821738702, 34.67381673639106], [-82.84565611167413, 34.6761813842436], [-82.84807573583119, 34.68216965456513]]])