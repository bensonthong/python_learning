# Chapter 5 If Statements

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("=================================================")
# Conditional Test - True , False
# if True: if statement will run, if False -> else statement will run
age = 18
print(age == 18)
print(age == 17)
print(age != 17)

# Checking multiple conditions
age_0 = 21
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
print("=================================================")
# Check if a value is in a list
pizza = ["pineapple", "pepperoni", "cheese", "veggie"]
print("pineapple" in pizza)

# Elif statements
age = 18
if age > 18:
    print("You are an adult")
elif age == 18:
    print("Congratulations you are now an adult")
elif 13 < age < 18  # age > 13 and age < 18
    print("You are a teen ")
else:
    print("You are not an adult")

