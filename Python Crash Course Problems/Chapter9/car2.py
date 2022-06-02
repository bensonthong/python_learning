class Car2:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value, Reject it if attempts to roll back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print(f"This car has {mileage} miles on it")
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to an odometer"""
        self.odometer_reading += miles


my_new_car = Car2('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# To Modify Attribute Values
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Or through a created method
my_new_car.update_odometer(26)
my_new_car.increment_odometer(500)
my_new_car.read_odometer()
