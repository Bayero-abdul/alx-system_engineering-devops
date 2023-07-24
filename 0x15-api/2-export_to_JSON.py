#!/usr/bin/python3
"""This module contains a Python script that, using this REST API,
for a given employee ID and stores it in a json file

"""

import csv
import json
import requests
import sys


def main():
    """main function"""
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        id = sys.argv[1]
        todo_response = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id))
        user_response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(id))

        if todo_response.status_code == 200 and \
                user_response.status_code == 200:
            todos = todo_response.json()
            user = user_response.json()
            username = user.get('username')

            dict = {id: [{"task": task.get('title'), "completed": task.get(
                'completed'), 'username': username} for task in todos]}

            with open('{}.json'.format(id), 'w') as json_file:
                json.dump(dict, json_file)


if __name__ == '__main__':
    main()
