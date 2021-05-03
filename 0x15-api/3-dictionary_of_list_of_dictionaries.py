#!/usr/bin/python3
"""
Module to Gather data from an API (jsonplaceholder.typicode.com)
"""
import requests
from sys import argv
import json


def main():
    """
    Request data from API and print to stdout
    """
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    task_data = response_todos.json()
    url = 'https://jsonplaceholder.typicode.com/users/'
    response_users_info = requests.get(url)
    users_info = response_users_info.json()

    tasks_by_employee = {}
    for user in users_info:
        task_user_list = []
        for task in task_data:
            if task['userId'] == user['id']:
                task_dict = {}
                task_dict['task'] = task['title']
                task_dict['completed'] = task['completed']
                task_dict['username'] = user['username']
                task_user_list.append(task_dict)
        tasks_by_employee[user['id']] = task_user_list

    with open("todo_all_employees.json", "w") as write_file:
        json.dump(tasks_by_employee, write_file)

if __name__ == "__main__":
    main()
