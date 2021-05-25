temperature = 45
if temperature > 30:
    print("It is a hot day")
elif temperature < 10:
    print("It is a cold day")
else:
    print("It is neither hot nor cold")

# equality operator: ==
# comparison operators , >, < ,>=, <= , !, !=

name = "Jason"

print(len(name))
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")