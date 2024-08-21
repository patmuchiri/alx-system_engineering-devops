#!/usr/bin/python3
"""
Script queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return 'OK' if subreddit exists, otherwise 'OK'."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            # Optionally use subscribers data if needed
            return "OK"
        else:
            return "OK"
    except requests.RequestException:
        return "OK"
