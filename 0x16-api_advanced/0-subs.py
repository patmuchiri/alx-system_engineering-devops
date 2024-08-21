#!/usr/bin/python3
"""
provides a fxn to query the Reddit API and get no of subs for given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the no of subs for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: no of subscribers if the subreddit is valid, 0 otherwise.
    """
    # Define the Reddit API endpoint for the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'myRedditBot/1.0'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response to extract the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # Return 0 for invalid subreddits or any other errors
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
