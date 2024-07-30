#!/usr/bin/python3

""" Export this to JSON """

from requests import get
import json


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    res = get(url)
    users = res.json()

    data = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        res = get(url)
        tasks = res.json()

        data[user_id] = []

        for task in tasks:
            data[user_id].append({
                                  "username": username,
                                  "task": task.get('title'),
                                  "completed": task.get('completed')
                                  })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
