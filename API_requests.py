import requests
import os
from datetime import datetime, timedelta

#access_token = "prj_test_pk_06ec8e7a8c4daef4b2cdab70b145c68c515431fa"
access_token = "prj_test_sk_54ed50a4e9e77cde4b4708250e916a3ce27de10b"
def get_json(url,params):
    response = requests.get(
    url,
    params=params,
    headers={"Authorization": "{}".format(access_token)},
    )

    json_response = response.json()

    return json_response
print(get_json("https://api.radar.io/v1/users",{}))
