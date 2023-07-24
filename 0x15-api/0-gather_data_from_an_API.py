#!/usr/bin/python3
"""This module contains a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.

"""

import requests
import sys


def main():
    """main function"""
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        id = int(sys.argv[1])
        todo_response = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id))
        user_response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(id))

        if todo_response.status_code == 200 and \
                user_response.status_code == 200:
            todos = todo_response.json()
            user = user_response.json()
            name = user.get('name')

            total_tasks = len(todos)
            task_done_cnt = 0
            for task in todos:
                if task.get('completed'):
                    task_done_cnt += 1

            print("Employee {} is done with tasks({}/{}):"
                  .format(name,
                          task_done_cnt,
                          total_tasks))

            for task in todos:
                if task.get('completed'):
                    print("\t {}".format(task.get('title')))


if __name__ == '__main__':
    main()
