#!/usr/bin/python3
"""
module: queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers (not active users, total subscribers) for a given subreddit
    """
    headers = {
        "User-Agent": "Github/1.0 by Bayero-abdul (Contact: bayeroa65@gmail.com)"
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(
        url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        return (data['subscribers'])
    else:
        return (0)
