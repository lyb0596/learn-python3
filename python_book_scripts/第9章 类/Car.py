#9.2　使用类和实例
class Car():
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage



my_new_car = Car('BMW','X5',2017)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 9.2.3　修改属性的值
# 可以以三种不同的方式修改属性的值：直接通过实例进行修改；通过方法进行设置；通过方法进行递增（增加特定的值）。
    # 1. 直接修改属性的值
my_new_car.odometer_reading = 3
my_new_car.read_odometer()
    # 2. 通过方法修改属性的值
my_new_car.update_odometer(33)
my_new_car.read_odometer()
