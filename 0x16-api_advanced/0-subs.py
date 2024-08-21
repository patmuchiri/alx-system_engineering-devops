#!/usr/bin/python3

"""How many subscribers?"""

from requests import get


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/123.0.0.0 Safari/537.36'
            }

    res = get(url, headers=headers).json()

    try:
        subs = res.get('data').get('subscribers')
        return int(subs)
    except Exception:
        return 0
