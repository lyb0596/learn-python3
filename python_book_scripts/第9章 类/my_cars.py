# 9.4.3　从一个模块中导入多个类
from electric_car import Car,ElectricCar

my_car1 = Car('volkswagen', 'beetle', 2016)
print(my_car1.get_descriptive_name())

my_car2 = ElectricCar('volkswagen', 'beetle', 2016)
print(my_car2.describe_battery())
print(my_car2.get_descriptive_name())
