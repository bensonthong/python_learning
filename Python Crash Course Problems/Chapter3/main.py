# Chapter 3 List
# 3-1
names = ['bob', 'james', 'eric', 'john']
print(names)
print(names[0].title())
print(names[1].title())
print(names[2].title())

print(f"Hello {names[0].title()}, you are awesome!")
print(f"Hello {names[1].title()}, you are awesome!")
print(f"Hello {names[2].title()}, you are awesome!")

# Modifying List
names[0] = 'Manny'
print(names)

# Adding to list
names.append('Jeremy')
print(names)

# Using insert method
names.insert(1, 'Jeremy')   # index, value
print(names)

# removing elements
del names[0]
print(names)

print("========================================")
# pop method allows you to remove an item from the list
# but with the feature of allowing you to modify the item
popped_value = names.pop()
print(names)
print(popped_value)

# 3-4 Guest List
invite = ['Mary', 'Jane', 'Larry', 'Ivan']
for person in invite:
    print(f"You are invited to dinner {person}!")

print("========================================")
# Organizing a list using: sort() and reverse() method
cars = ['bmw', 'honda', 'toyota', 'mercedes']
cars.sort()
print(cars)

# Sort method can reverse by alphabetical order too
cars.sort(reverse=True)
print(cars)
print("========================================")
# Can also sort without changing list using sorted()
print(sorted(cars))
print(cars)

cars.reverse()
print(cars)

# Finding length of a list
print(len(cars))