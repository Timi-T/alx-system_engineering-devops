#!/usr/bin/python3
"""
testing getting data from an api
"""

import json
import requests
import sys


if __name__ == "__main__":
    id = int(sys.argv[1])
    users = 'https://jsonplaceholder.typicode.com/users?id={}'.format(id)
    todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
    user_response = requests.get(users)
    todo_response = requests.get(todo)

    data = todo_response.text
    tasks = json.loads(data)
    user = user_response.text
    user = json.loads(user)
    name = user[0].get('name')

    complt = 0
    all = len(tasks)
    for task in tasks:
        if task.get('completed') is True:
            complt += 1
    print("Employee {} is done with tasks ({}/{})".format(name, complt, all))
    for task in tasks:
        if task.get('completed') is True:
            print("\t{}".format(task.get('title')))
