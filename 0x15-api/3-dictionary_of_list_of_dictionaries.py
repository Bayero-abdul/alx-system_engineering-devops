#!/usr/bin/python3
"""This module contains a Python script that, using this REST API,
gets all users detail and stores it in a json file

"""

import json
import requests


def main():
    """main function"""
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    if users_response.status_code == 200:
        users = users_response.json()
        dict = {}
        for user in users:
            id = user.get('id')
            todo_response = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'
                .format(id))
            if todo_response.status_code == 200:
                todos = todo_response.json()
                username = user.get('username')

                dict[id] = [{'username': username, "task": task.get(
                             'title'), "completed": task.get('completed')}
                            for task in todos]

        with open('todo_all_employees.json'.format(id), 'w') as json_file:
            json.dump(dict, json_file)


if __name__ == '__main__':
    main()
