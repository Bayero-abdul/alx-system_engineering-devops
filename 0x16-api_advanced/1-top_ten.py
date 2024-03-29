#!/usr/bin/python3
"""
module: queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Returns the titles of
    the first 10 hot posts listed for a given subreddit
    """
    if (subreddit is None):
        print(None)
        return

    headers = {
        "User-Agent": "Github/1.0 by Bayero-abdul \
        (Contact: bayeroa65@gmail.com)"
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        if data is None:
            print(None)
            return
        top = data.get('children')[:10]
        if top is None:
            print(None)
            return

        for i in range(10):
            print(top[i].get('data').get('title'))
    else:
        print(None)
