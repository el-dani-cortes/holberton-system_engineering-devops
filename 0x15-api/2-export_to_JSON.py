#!/usr/bin/python3
"""
Module to Gather data from an API (jsonplaceholder.typicode.com)
"""
import json
import requests
from sys import argv


def main(argv):
    """
    Request data from API and print to stdout
    """
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    task_data = response_todos.json()
    url = 'https://jsonplaceholder.typicode.com/users/'
    response_user_info = requests.get(url + argv[1])
    user_info = response_user_info.json()
    name = user_info['name']
    user_name = user_info['username']

    task_user_list = []
    for task in task_data:
        if task['userId'] == int(argv[1]):
            task_dict = {}
            task_dict['task'] = task['title']
            task_dict['completed'] = task['completed']
            task_dict['username'] = user_name
            task_user_list.append(task_dict)

    tasks_by_employee = {}
    tasks_by_employee[argv[1]] = task_user_list

    with open("{}.json".format(argv[1]), "w") as write_file:
        json.dump(tasks_by_employee, write_file)

if __name__ == "__main__":
    main(argv)
