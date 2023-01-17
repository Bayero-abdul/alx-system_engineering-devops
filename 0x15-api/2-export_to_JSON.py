#!/usr/bin/python3
"""using this REST API, or a given employee ID,
return information about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == '__main__':

    id = int(sys.argv[1])
    API = 'https://jsonplaceholder.typicode.com'
    json_todos = requests.get(API + '/todos').json()
    u_name = requests.get(API + '/users/' + str(id)).json().get('username')

    tasks = list(filter(lambda u_id: u_id.get('userId') == id,
                        json_todos))

    user_dict = {str(id): [{"task": x.get("title"),
                            "completed": x.get("completed"),
                            "username": u_name} for x in tasks]}

    with open(str(id)+'.json', 'w') as f:
        f.write(json.dumps(user_dict))
