#!/usr/bin/python3
"""
Module that contains the function recurse
"""


import requests


def recurse(subreddit, hot_list=[], after=""):
    """Recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-agent': 'Adventurous-Bed5688'}
    param = {'after': after}
    req = requests.get(url, headers=header, params=param,
                       allow_redirects=False)
    if req.status_code > 300:
        return None

    for i in req.json().get('data').get('children'):
        hot_list.append(i.get('title'))

    if req.json().get('data').get('after') is not None:
         return recurse(subreddit, hot_list, after)
    return hot_list
