import requests
def get_json(url,params):
    response = requests.get(
    url,
    params=params
    )

    json_response = response.json()

    return json_response
print(get_json('http://www.127.0.0.1:3000/',{}))