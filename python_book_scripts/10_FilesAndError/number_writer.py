# 10.4　存储数据 10.4.1　使用json.dump() 和json.load()
import json
numbers = [2, 3, 5, 7, 11, 13]

filename = 'pi_digits'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

with open(filename) as r_obj:
    print(json.load(r_obj))