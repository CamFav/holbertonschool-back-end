#!/usr/bin/python3
""" def """
import csv
import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]

    """Get employee information"""
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = response.json()
    employee_name = employee_data['name']
    employee_username = employee_data['username']

    """Get todo list"""
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos = response.json()

    
    """Data to JSON."""
    file = "todo_all_employees.json"
    tasks = []
    for todo in todos:
        title = todo.get("title")
        completed = todo.get("completed")
        tasks.append({"username": employee_username, "task": title, "completed": completed})

    data = {employee_id: tasks}

    with open("todo_all_employees.json", "a+") as file:
        json.dump(data, file)
