#!/usr/local/bin/python3

"""
get subreddits from the reddit api
"""

import json
import requests


def number_of_subscribers(subreddit):
    """
    check the number of  subscribers to a certain subreddit
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "opesUserAgent"}
    r = requests.get(url, allow_redirects=False, headers=headers)
    if (r.status_code == 200):
        r_json = json.loads(r.text)
        no_of_sub = r_json['data']['subscribers']
        return no_of_sub
    return 0
