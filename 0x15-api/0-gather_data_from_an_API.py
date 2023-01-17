#!/usr/bin/python3
"""using this REST API, or a given employee ID,
return information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == '__main__':

    id = int(sys.argv[1])
    API = 'https://jsonplaceholder.typicode.com'
    json_todos = requests.get(API + '/todos').json()
    u_name = requests.get(API + '/users/' + str(id)).json().get('name')

    tasks = list(filter(lambda u_id: u_id.get('userId') == id,
                        json_todos))
    tasks_done = list(filter(lambda u_id: u_id.get('completed'),
                             tasks))

    print('Employee {} is done with tasks({}/{}):'.format(
            u_name, len(tasks_done), len(tasks)))

    for x in tasks_done:
        print('\t {}'.format(x.get('title')))
