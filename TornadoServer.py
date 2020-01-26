from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import tornado.escape
import json
import requests
from datetime import datetime
import os

access_token = "prj_test_sk_54ed50a4e9e77cde4b4708250e916a3ce27de10b"
access_token_2 = "prj_live_sk_1a4edf50f41968460a79e7de135e3e45ed83d018"

def get_json(url,params):
    response = requests.get(
    url,
    params=params,
    headers={"Authorization": "{}".format(access_token)},
    )

    json_response = response.json()

    return json_response

def post_json(url,payload,token):
    post = requests.post(
    url,
    data=payload,
    headers={"Authorization": "{}".format(token)},
    )
    json_response = post.json()
    return json_response
def clean_geo(rawcode):
    data={}
    data['points']=[]
    for i in range(0,len(rawcode['geofences'])):
        data['points'].append({'Coordinates':rawcode['geofences'][i]['geometryCenter']['coordinates']})
    return data
def pull_geospace():
    return get_json('https://api.radar.io/v1/geofences',{})
def upload_polygon(parameters): #Parameters in [name,tag,coordinates] strings Coordinates in [[],[],...]
    current = datetime.now()
    name = parameters['name']
    tag = parameters['tag']
    coordinates = parameters['coordinates']
    payload = {'description' : name, 'type' : 'circle', 'coordinates' : coordinates, 'radius' : 50, 'tag' : tag, 'externalId' : current.strftime("%d%H%M%S")} #send geospaces back to client after this
    post_json('https://api.radar.io/v1/geofences',payload,access_token_2)
    post_json('https://api.radar.io/v1/geofences',payload,access_token)
    return pull_geospace()
def date_clean(data):
    current = datetime.now()
    day = int(current.strftime("%d"))
    for i in range(0,len(data['geofences'])):
        if (day - int(data['geofences'][i]['externalId'][0:2])) != 0:
            requests.delete("https://api.radar.io/v1/geofences/"+"{}".format(data['geofences'][i][' id']),
                headers={"Authorization": "{}".format(access_token)}
                )
        else:
            continue

class TodoItems(RequestHandler):
    def get(self):
        date_clean(pull_geospace())
        pull_geospace()
        self.write(tornado.escape.json_encode(clean_geo(pull_geospace())))
    def post(self):
        message = tornado.escape.json_decode(self.request.body)
        upload_polygon(message)
        date_clean(pull_geospace())
        self.write(tornado.escape.json_encode(clean_geo(pull_geospace())))

def make_app():
    urls = [
        ("/", TodoItems)
        ]
    return Application(urls, debug=True)
  
if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()