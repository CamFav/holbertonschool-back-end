#!/usr/bin/python3
"""Modules"""
import csv
import requests
import sys


def employee_todo(employee_id):
    """_summary_

    Args:
        employee_id (_type_): _description_
    """
    api_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{api_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data["name"]

    todos_response = requests.get(f"{api_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = [todo for todo in todos_data if todo["completed"]]

    antonette = f"{employee_id}.csv"

    with open(antonette, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in completed_tasks:
            csv_writer.writerow([user_data["id"], user_data["username"], task["completed"], task["title"]])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        employee_todo(employee_id)
