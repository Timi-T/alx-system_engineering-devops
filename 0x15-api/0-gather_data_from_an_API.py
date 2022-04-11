#!/usr/bin/python3
"""
testing getting data from an api
"""

import json
import requests
import sys


if __name__ == "__main__":
    id = int(sys.argv[1])
    users = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    todo = 'https://jsonplaceholder.typicode.com/todos'
    user_response = requests.get(users)
    todo_response = requests.get(todo)

    data = todo_response.text
    tasks = json.loads(data)
    user = user_response.text
    user = json.loads(user)
    nm = user.get('name')

    all = 0
    cm = 0
    for task in tasks:
        if task['userId'] == id:
            all += 1
            if task.get('completed') is True:
                cm += 1
    print("Employee {} is done with tasks({}/{}):".format(nm, cm, all))
    for task in tasks:
        if task['userId'] == id and task.get('completed') is True:
            print("\t {}".format(task.get('title')))
