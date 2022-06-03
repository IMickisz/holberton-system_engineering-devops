#!/usr/bin/python3
"""
Module that contains the function number_of_subscribers.
"""


import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number of
    subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers={'User-agent': 'Adventurous-Bed5688'},
                       allow_redirects=False)
    if req.status_code > 300:
        return 0
    return(req.json().get('data').get('subscribers'))
