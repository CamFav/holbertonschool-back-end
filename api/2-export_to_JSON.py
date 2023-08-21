#!/usr/bin/python3
"""Modules"""
import requests
import json
import sys


def employee_todo(employee_id):
    """_summary_

    Args:
        employee_id (_type_): _description_
    """
    api_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{api_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_username = user_data["username"]

    todos_response = requests.get(f"{api_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    tasks_list = []
    for task in todos_data:
        task_info = {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_username
        }
        tasks_list.append(task_info)

    employee_tasks = {str(employee_id): tasks_list}

    json_filename = f"{employee_id}.json"
    with open(json_filename, "w") as json_file:
        json.dump(employee_tasks, json_file)
  

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        employee_todo(employee_id)
