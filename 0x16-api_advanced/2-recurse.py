#!/usr/bin/python3
"""
provides a recursive function to query the Reddit API and return list
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API and return a list of titles.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to accumulate the titles of hot articles.
        after (str): The Reddit API parameter for pagination (optional).

    Returns:
        list of titles of hot articles if subreddit is valid, None otherwise.
    """
    # Define the Reddit API endpoint for the given subreddit, for pagination
    url = (
        f"https://www.reddit.com/r/{subreddit}/hot.json"
        f"?limit=100&after={after}"
    )
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'myRedditBot/1.0'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response to extract the titles
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']

        if posts:
            # Accumulate the titles of the current page's hot articles
            hot_list.extend([post['data']['title'] for post in posts])

            # If there's an 'after' parameter, recursively call the fxn
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return hot_list
    else:
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
