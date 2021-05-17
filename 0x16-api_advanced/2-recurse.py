#!/usr/bin/python3
"""
Module to request information from reditt API about any subreddit recursively
"""
import requests


def recurse(subreddit, hot_list=[], params={}):
    """
    Method to request and get all hot posts listed for a
    given subreddit recursively.
    """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    headers = {
        'User-agent': "just me"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return (None)

    information = response.json()
    data = information["data"]
    children = data["children"]
    for post in children:
        hot_list.append(post["data"]["title"])
    params["after"] = data["after"]

    if params["after"] is not None:
        recurse(subreddit, hot_list, params)
    return(hot_list)
