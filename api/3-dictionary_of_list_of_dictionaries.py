#!/usr/bin/python3
""" def """
import csv
import json
import requests
import sys


if __name__ == '__main__':
    """Get employee information"""
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users")
    employees = response.json()

    """Get todo list"""
    data = {}
    for employee in employees:
        employee_id = employee['id']
        employee_username = employee['username']
        employee_name = employee['name']
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
        todos = response.json()

        tasks = []
        for todo in todos:
            title = todo.get("title")
            completed = todo.get("completed")
            tasks.append({"username": employee_username, "task": title, "completed": completed})

        data[str(employee_id)] = tasks

    """Data to JSON."""
    with open("todo_all_employees.json", "w") as file:
        json.dump(data, file, indent=4)
