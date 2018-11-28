from collections import OrderedDict
# 调用OrderedDict() 来创建一个空的有序字典
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sa'] = 'c'

for name,language in favorite_languages.items():
    print(name.title() + '  ' + language.title())
