import json

file_name = 'username'
username = input("input your name: ")
with open(file_name, 'w') as f_obj:
    json.dump(username, f_obj)

