import requests
import json
def get_json(url,params):
    response = requests.get(
    url,
    params=params
    )

    json_response = response.json()

    return json_response
def post_json(url,payload):
    post = requests.post(
    url,
    data=payload,
    )
    json_response = post.json()
    return json_response
print(post_json('http://127.0.0.1:3000/',json.dumps({'name' : 'nope', 'tag' : 'geat', 'coordinates' : [-82.84807573583119, 34.68216965456513]})))
# def clean_geo(rawcode):
#     data={}
#     data['instances']=[]
#     for i in range(0,len(rawcode['geofences'])):
#         data['instances'].append({'Coordinates':rawcode['geofences'][i]['geometryCenter']['coordinates']})
#     return data
# print(clean_geo(georeq.pull_geospace()))
# b = '1278391273'
# print(b[0:2]+"2")