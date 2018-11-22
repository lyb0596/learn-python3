class Dog():
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + "is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

# 通常可以认为首字母大写的名称（如Dog ）指的是类，而
# 小写的名称（如my_dog ）指的是根据类创建的实例。
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 根据Dog 类创建实例后，就可以使用句点表示法来调用Dog 类中定义的任何方法
my_dog.sit()
my_dog.roll_over()
