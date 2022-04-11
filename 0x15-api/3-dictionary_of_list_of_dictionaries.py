#!/usr/bin/python3
"""
testing getting data from an api
"""

import json
import requests


if __name__ == "__main__":
    users = 'https://jsonplaceholder.typicode.com/users'
    todo = 'https://jsonplaceholder.typicode.com/todos'
    user_response = requests.get(users)
    todo_response = requests.get(todo)

    data = todo_response.text
    tasks = json.loads(data)
    users = user_response.text
    users = json.loads(users)
    output_file = 'todo_all_employees.json'

    json_dict = {}
    for user in users:
        name = user.get('username')
        id = user.get('id')

        task_list = []
        for task in tasks:
            if task.get('userId') == id:
                new_dict = {}
                new_dict['task'] = task.get('title')
                new_dict['completed'] = task.get('completed')
                new_dict['username'] = name
                task_list.append(new_dict)
        json_dict[str(id)] = task_list
    with open(output_file, 'w') as f:
        json.dump(json_dict, f)
