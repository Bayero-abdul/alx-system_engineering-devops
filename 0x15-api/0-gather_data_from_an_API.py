#!/usr/bin/python3

"""display on the standard output the employee TODO list progress."""


def main():
    import requests
    import sys

    try:
        id = int(sys.argv[1])
    except TypeError:
        print("argument must be int")

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    json_todos = todos.json()
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    json_users = users.json()

    name = get_name(id, json_users)
    cnt_done, cnt_tasks, titles = get_employee_details(id, json_todos)

    title_string = ""
    for i in range(len(titles)):
        if i == len(titles) - 1:
            title_string += titles[i]
        else:
            title_string += titles[i] + '\n\t'

    output = f'Employee {name} is done with tasks({cnt_done}/{cnt_tasks}):\
               \n\t{title_string}'
    print(output)


def get_name(id, json_users):
    """get name of id"""

    for user in json_users:
        if user.get('id') == id:
            return user.get('name')
    return ""


def get_employee_details(id, json_todos):
    """return employee details"""

    cnt_done = 0
    cnt_tasks = 0
    titles = []
    state = 0

    for user in json_todos:
        if user.get('userId') == id and user.get('completed'):
            state = 1
            cnt_done += 1
            cnt_tasks += 1
            titles.append(user.get('title'))
        elif user.get('userId') == id:
            state = 1
            cnt_tasks += 1
        elif state == 1:
            break

    return (cnt_done, cnt_tasks, titles)


if __name__ == '__main__':
    main()
