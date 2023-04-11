#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    url_todos = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)

    response_user = requests.get(url_user)
    response_todos = requests.get(url_todos)

    user_name = response_user.json().get("username")
    todos = response_todos.json()

    todo_list = []
    for task in todos:
        title = task.get("title")
        completed = task.get("completed")
        todo_list.append({"username": user_name, "task": title, "completed": completed})

    data = {user_id: todo_list}

    with open("todo_all_employees.json", "a+") as file:
        json.dump(data, file)
