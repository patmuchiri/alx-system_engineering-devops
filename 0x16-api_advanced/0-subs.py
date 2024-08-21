#!/usr/bin/python3
"""
this script queries subscibers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except requests.RequestException:
        return 0
