#!/usr/bin/python3
"""This module contains a Python script that, using this REST API,
for a given employee ID and stores it in a CSV file

"""

import csv
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
            username = user.get('username')

            with open('{}.csv'.format(id), 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_ALL)

                for task in todos:
                    writer.writerow([id, username, task.get(
                        'completed'), task.get('title')])


if __name__ == '__main__':
    main()
