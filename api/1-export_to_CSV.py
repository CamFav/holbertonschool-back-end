#!/usr/bin/python3
""" def """
import requests
import sys
import csv


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
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todos = response.json()
    todo_title = todos['title']
    todo_completed = todos['completed']

    """Count completed tasks"""
    completed_tasks = []
    for todo in todos:
        if todo['completed']:
            completed_tasks.append(todo)
    done_tasks = len(completed_tasks)
    total = len(todos)

    print(
        f"Employee {employee_name} is done with tasks({done_tasks}/{total}):")

    for todo in completed_tasks:
        print(f"\t", {todo['title']})

    """Data to CSV."""
    file = f"{employee_id}.csv"
    with open(file, mode='w') as csv_file:
        my_writer = csv.writer(csv_file)
        for todo in completed_tasks:
            my_writer.writerow([employee_id, employee_username, todo_completed, todo_title])
