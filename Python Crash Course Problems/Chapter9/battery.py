class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        if self.battery_size == 75:
            r = 260
        elif self.battery_size == 100:
            r = 315

        print(f"This car can go about {r} miles on a full charge")