#!/usr/bin/python3

"""The Top ten hot posts"""

from requests import get


def recurse(subreddit, hot_list=[]):
    """ recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/123.0.0.0 Safari/537.36'
            }

    res = get(url, headers=headers, allow_redirects=False).json()

    try:
        children = res.get('data').get('children')
        for title in children:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    except Exception:
        return None
