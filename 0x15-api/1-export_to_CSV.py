#!/usr/bin/python3
"""using this REST API, or a given employee ID,
put the information about his/her TODO list progress
in a CSV file.
"""
import csv
import requests
import sys


if __name__ == '__main__':

    id = int(sys.argv[1])
    API = 'https://jsonplaceholder.typicode.com'
    json_todos = requests.get(API + '/todos').json()
    u_name = requests.get(API + '/users/' + str(id)).json().get('name')

    tasks = list(filter(lambda u_id: u_id.get('userId') == id,
                        json_todos))
    data = [{'id': x.get("userId"),
             'name': u_name,
             'completed': x.get("completed"),
             'title': x.get("title")
             } for x in tasks]

    with open(f'{id}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames=["id",
                                            "name",
                                            "completed",
                                            "title"],
                                delimiter=",",
                                quoting=csv.QUOTE_ALL)
        for row in data:
            writer.writerow(row)
