#!/usr/bin/python3

""" Gather data from the API """

from requests import get
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    res = get(url)
    name = res.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    res = get(url)
    tasks = res.json()

    completed = 0
    completed_tasks = []

    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, len(tasks)))

    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))
