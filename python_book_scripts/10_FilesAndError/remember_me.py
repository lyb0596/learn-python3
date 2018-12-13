#-*- coding:utf-8 -*-

import json

def get_stored_username():
    file_name = 'username'
    try:
        with open(file_name) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        pass
    else:
        return username

def get_new_username():
    file_name = 'username'
    username = input("input your name: ")
    with open(file_name, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()