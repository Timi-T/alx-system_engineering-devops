#!/usr/local/bin/python3
"""
Get word count from all hot posts from reddit api given a subreddit
"""

import json
import requests


def recurse(subreddit, word_list, hot_list=[], response='', count=0, after=''):
    """
    list word count of hottest posts from subreddit

    """

    """Base case"""
    if (after is None):
        return

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
    recurse(subreddit, word_list, hot_list, response, count + 1, after)
    return hot_list


def count_words(subreddit, word_list, hot_list=[],
                response='', count=0, after=''):
    """
    caller function for recursive function
    """

    hot_list = recurse(subreddit, word_list, hot_list=[],
                       response='', count=0, after='')
    if not (hot_list):
        return
    words_dict = {}
    for wd in word_list:
        words_dict[wd.lower()] = 0
    for title in hot_list:
        words = (title.lower()).split()
        for word in word_list:
            if word.lower() in words:
                words_dict[word.lower()] += 1
    x = dict(sorted(words_dict.items(), key=lambda
                    x: (x[1], x[0]), reverse=True))
    for k, v in x.items():
        if v != 0:
            print("{}: {}".format(k, v))
