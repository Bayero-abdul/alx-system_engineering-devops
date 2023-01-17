
#!/usr/bin/python3


def main():
    import request
    import sys

    if len(sys.argv) == 1:
       print("Usage: 0-gather_data_from_an_API.py (integer)")
    elif not isinstance(sys.argv[1], int):
        print("argument must be an integer")
    
    json_todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    json_users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    
    name = get_name(id, json_users)
    cnt_done, cnt_tasks, titles = get_employee_details(id, json_todos)

    title_string = ""
    for i in range(len(titles)):
        if i != len(titles) - 1:
            title_string += title[i] + "\t\n"
        else:
            title_string += title[i] + "\n"
      
    output = f'Employee {name} is done with tasks{cnt_done/cnt_tasks}:\t\n{title_string}'
    print (output)


def get_name (id, json_users):

    for user in json_users:
        if json.get('id') == id:
            return json.get(name)
    return ""


def get_employee_details(id, json_todos):
    
    cnt_done = 0
    cnt_tasks = 0
    titles = []
    STATE = 0
    
    for user in json_todos:
        if json.get('id') == id and json.get('completed') == true:
            state = 1
            cnt_done += 1
            cnt_tasks += 1
            titles.append(json)
        elif json.get('id') == id:
            state = 1
            cnt_tasks += 1
        elif state == 1:
            break

    return (cnt_done, cnt_tasks, titles)

