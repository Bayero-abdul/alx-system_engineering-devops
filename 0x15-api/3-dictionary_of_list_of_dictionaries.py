#!/usr/bin/python3
"""Records all tasks from all employees
in json format
"""
import json
import requests
import sys


if __name__ == '__main__':

    API = 'https://jsonplaceholder.typicode.com'
    json_todos = requests.get(API + '/todos').json()
    json_users = requests.get(API + '/users').json()

    users_dict = {}
    for user in json_users:
        id = user.get('id')
        tasks = list(filter(lambda u_id: u_id.get('userId') == id, json_todos))

        users_dict[str(id)] = [{"task": x.get("title"),
                                "completed": x.get("completed"),
                                "username": user.get('username')
                                } for x in tasks]

    with open('todo_all_employees.json', 'w') as f:
        f.write(json.dumps(users_dict))
