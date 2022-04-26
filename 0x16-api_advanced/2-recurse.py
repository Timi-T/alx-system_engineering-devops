#!/usr/bin/python3
"""
Get all hot posts from reddit api given a subreddit
"""

import json
import requests


def recurse(subreddit, hot_list=[], response='', count=0, after=''):
    """
    list hottest posts from subreddit
    """

    """Base case"""
    if (after is None):
        done = 1

    url = "https://www.reddit.com/r/{}/hot.json\
?after={}&limit=100".format(subreddit, after)
    headers = {"User-Agent": "opesUserAgent"}

    """For first page"""
    if (count == 0):
        response = requests.get(url, allow_redirects=False, headers=headers)
    elif (len(after) > 0):
        """For other pages"""
        response = requests.get(url, allow_redirects=False, headers=headers)
        after = ''

    """Upon success"""
    if (response.status_code == 200):
        r_json = json.loads(response.text)
        try:
            hot_list.append(r_json['data']['children'][count]['data']['title'])
        except IndexError:
            count = -1
            after = r_json['data']['after']
    else:
        return None
    recurse(subreddit, hot_list, response, count + 1, after)
    return (hot_list)
