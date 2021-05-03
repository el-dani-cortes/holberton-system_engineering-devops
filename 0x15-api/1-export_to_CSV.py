#!/usr/bin/python3
"""
Module to Gather data from an API (jsonplaceholder.typicode.com)
"""
import csv
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

    with open('{}.csv'.format(argv[1]), mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',',
                                     quotechar='"', quoting=csv.QUOTE_ALL)
        for task in task_data:
            if task['userId'] == int(argv[1]):
                employee_writer.writerow([task['userId'], user_name,
                                          task['completed'], task['title']])


if __name__ == "__main__":
    main(argv)
