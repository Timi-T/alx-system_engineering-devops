#!/usr/local/bin/python3
"""
Get top ten hot posts from reddit api given a subreddit
"""

import requests
import json


def top_ten(subreddit):
    """
    list ten hottest posts from subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "opesUserAgent"}
    response = requests.get(url, allow_redirects=False, headers=headers)

    if (response.status_code == 200):
        r_json = json.loads(response.text)
        for post in r_json['data']['children']:
            title = post['data']['title']
            print(title)
    else:
        print(None)
