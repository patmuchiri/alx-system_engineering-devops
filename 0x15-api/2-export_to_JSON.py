#!/usr/bin/python3

""" Export to the JSON file """

from requests import get
import json
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    res = get(url)
    username = res.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    res = get(url)
    tasks = res.json()

    data = {user_id: []}

    for task in tasks:
        data[user_id].append({
                              "task": task.get('title'),
                              "completed": task.get('completed'),
                              "username": username
                              })

    with open('{}.json'.format(user_id), 'w') as file:
        json.dump(data, file)
