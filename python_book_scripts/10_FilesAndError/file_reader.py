#-*- coding:utf-8 -*-
with open(r'.\pi_digits') as file_object:

    # contents = file_object.read()
    # print(contents.strip())

# 10.1.3　逐行读取
    # for line in file_object:
    #     print(line.rstrip())

# 10.1.4　创建一个包含文件各行内容的列表,readline一个个字符读取
#     lines = file_object.readlines()
#     for line in lines:
#         print(line.rstrip())

# 将文件读取到内存中
#     lines = file_object.readlines()
#     pi_string = ''
#     for line in lines:
#         pi_string += line.rstrip()
#     print(pi_string)

# 10.1.7　圆周率值中包含你的生日
    pi_string = ''

    lines = file_object.readlines()
    for line in lines:
        pi_string += line.rstrip()
    birthday = input('input your birthday: ')
    if birthday in pi_string:
        print('yes')
    else:
        print('no')