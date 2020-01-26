import requests
import json
import georeq
from datetime import datetime
# def get_json(url,params):
#     response = requests.get(
#     url,
#     params=params
#     )

#     json_response = response.json()

#     return json_response
# def post_json(url,payload):
#     post = requests.post(
#     url,
#     data=payload,
#     )
#     json_response = post.json()
#     return json_response
# print(post_json('http://127.0.0.1:3000/',json.dumps({'name' : 'nope', 'tag' : 'geat', 'coordinates' : [-82.84807573583119, 34.68216965456513]})))
# def clean_geo(rawcode):
#     data={}
#     data['instances']=[]
#     for i in range(0,len(rawcode['geofences'])):
#         data['instances'].append({'Coordinates':rawcode['geofences'][i]['']})
#     return data
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
date_clean(georeq.pull_geospace())
# b = '1278391273'
# print(b[0:2]+"2")