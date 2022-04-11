#!/usr/bin/python3
"""
testing getting data from an api
"""

import requests
import json
import sys


id = int(sys.argv[1])
url_users = 'https://jsonplaceholder.typicode.com/users?id={}'.format(id)
url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
user_response = requests.get(url_users)
todo_response = requests.get(url_todo)


data = todo_response.text
tasks = json.loads(data)
user = user_response.text
user = json.loads(user)
name = user[0].get('name')

completed = 0
total = len(tasks)
for task in tasks:
    if task.get('completed') is True:
        completed += 1
print("Employee {} is done with tasks ({}/{})".format(name, completed, total))
for task in tasks:
    if task.get('completed') is True:
        print("\t{}".format(task.get('title')))
