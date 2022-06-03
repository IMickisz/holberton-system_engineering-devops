#!/usr/bin/python3
"""function that return the top 10 post from a subreddit"""

import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    req = requests.get(url, headers={"User-Agent": "Adventurous-Bed5688"},
                       allow_redirects=False)
    if req.status_code >= 300:
        print("None")
        return
    for i in req.json().get("data").get("children"):
        print(i.get("data").get("title"))
