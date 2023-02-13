#!/usr/bin/python3
import requests
import json
from datetime import datetime
import pysnowball as ball

import pysnowball.token as token


def fetch(url, host="xueqiu.com"):
    HEADERS = {'Host': host,
               'Accept': 'application/json',
               'Cookie': 'xq_a_token=e8624a78ef33301e3f439d5b2cb1aec0746a5ce4',
               'User-Agent': 'Xueqiu iPhone 11.8',
               'Accept-Language': 'zh-Hans-CN;q=1, ja-JP;q=0.9',
               'Accept-Encoding': 'br, gzip, deflate',
               'Connection': 'keep-alive'}

    response = requests.get(url, headers=HEADERS)

    # print(url)
    # print(HEADERS)
    # print(response)
    # print(response.content)

    if response.status_code != 200:
        raise Exception(response.content)

    return json.loads(response.content)

url = "https://xueqiu.com/v4/statuses/user_timeline.json?page=1&user_id=4111857140"
data=fetch(url)
for item in data['statuses']:
    print(item['description'] +   "\n")
    print(item['retweeted_status'] )
    print("-------------------------------------------")
