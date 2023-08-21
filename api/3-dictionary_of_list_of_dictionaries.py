#!/usr/bin/python3
"""Modules"""
import json
import requests
import sys


def export_todo_data():
    """_summary_

    Args:
        employee_id (_type_): _description_
    """
    api_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{api_url}/users")
    user_data = user_response.json()

    all_tasks = {}
    
    for user in user_data:
        user_id = user["id"]
        username = user["username"]
        
        todos_response = requests.get(f"{api_url}/todos?userId={user_id}")
        todos_data = todos_response.json()
        
        tasks_list = []
        for task in todos_data:
            task_info = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            tasks_list.append(task_info)

        all_tasks[str(user_id)] = tasks_list

    json_filename = "todo_all_employees.json"
    with open(json_filename, "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_todo_data()
