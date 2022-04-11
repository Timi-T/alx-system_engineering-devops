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
    name = user[0].get('username')

    with open('USER_ID.csv', 'w') as f:
        for task in tasks:
            st = task.get('status')
            tl = task.get('title')
            csv_txt = '"{}","{}","{}","{}"\n'.format(id, name, st, tl)
            f.write(csv_txt)
