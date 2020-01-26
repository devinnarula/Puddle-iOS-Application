import requests
def get_json(url):
    response = requests.get(
    url
    )

    json_response = response.json()

    return json_response
print(get_json("http://www.127.0.0.1:8888/"))