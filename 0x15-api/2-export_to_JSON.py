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

    output_file = '{}.json'.format(id)
    task_list = []
    with open(output_file, 'w') as f:
        for task in tasks:
            new_dict = {}
            new_dict['task'] = task.get('title')
            new_dict['completed'] = task.get('completed')
            new_dict['username'] = name
            task_list.append(new_dict)
        json_dict = {}
        json_dict[str(id)] = task_list
        json.dump(json_dict, f)
