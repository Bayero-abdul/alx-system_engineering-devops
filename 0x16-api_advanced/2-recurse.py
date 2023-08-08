#!/usr/bin/python3
"""
module: queries the Reddit API and returns the titles of
the first 10 hot article listed for a given subreddit
"""

import requests


def get_host_list_titles(L, i, size, hot_list=[]):
    """
    """
    if (i < size):
        hot_list.append(L[i].get('data').get('title'))
        i = i + 1
        get_host_list_titles(L, i, size, hot_list)
    return hot_list


def recurse_after(subreddit, hot_list=[], after=None):
    """
    Returns the titles of the hot articles listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "YourApp/1.0 by YourUsername (Contact: your@email.com)"
    }

    try:
        response = requests.get(url, headers=headers, params={"after": after})
        response.raise_for_status()  # Raise an exception if the request was unsuccessful

        data = response.json().get('data')
        kinds = data.get('children')
        hot_list = get_host_list_titles(kinds, 0, len(kinds), hot_list)

        # Get the "after" token from the response to fetch the next page
        after = data.get("after")

        if after:
            # Recursively call the function with the new "after" token
            return recurse_after(subreddit, hot_list, after)
        else:
            return hot_list

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


def recurse(subreddit, hot_list=[]):
    """
    Returns the titles of
    the hot articles listed for a given subreddit
    """
    return recurse_after(subreddit, hot_list=[])
