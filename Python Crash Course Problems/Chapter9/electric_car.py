from car import Car
from battery import Battery
# Inheritance


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

