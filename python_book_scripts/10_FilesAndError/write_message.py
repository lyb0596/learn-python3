#-*- coding:utf-8 -*-

with open(r'.\programming') as object:
    contents = object.readlines()
    print(contents)

# 10.2　写入文件
with open(r'.\programming','w') as file_object:
    file_object.write('abcd1')

#10.2.3　附加到文件
with open(r'.\programming','a') as file_a_object:
    file_a_object.write('345675*&')



with open(r'.\programming') as object:
    contents = object.readlines()
    print(contents)
