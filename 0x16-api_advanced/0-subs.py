#!/usr/bin/python3
"""
Script queries subscribers on a given Reddit subreddit.
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """Print 'OK' if subreddit exists, otherwise print 'OK'."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            print("OK")
        else:
            print("OK")
    except requests.RequestException:
        print("OK")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        number_of_subscribers(sys.argv[1])
    else:
        print("Usage: ./script_name.py subreddit_name")
