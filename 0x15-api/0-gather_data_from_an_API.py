#!/usr/bin/python3
"""
Module to Gather data from an API (jsonplaceholder.typicode.com)
"""
import requests
from sys import argv
from string import capwords


def main(argv):
    """
    Request data from API and print to stdout
    """
    task_completed = 0
    total_number_task = 0
    task_title_list = []
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    task_data = response_todos.json()
    for user in task_data:
        if user['userId'] == int(argv[1]):
            if user['completed'] is True:
                task_completed += 1
                task_title_list.append(user['title'])
            total_number_task += 1
    url = 'https://jsonplaceholder.typicode.com/users/'
    response_user_info = requests.get(url + argv[1])
    user_info = response_user_info.json()
    name = user_info['name']
    print('Employee {} is done with tasks({}/{}):'.format(name,
                                                          task_completed,
                                                          total_number_task))
    for title in task_title_list:
        print('\t {}'.format(title))

if __name__ == "__main__":
    main(argv)
