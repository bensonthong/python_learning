# Chapter 4 Looping in a List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print("Thank you, everyone. That was a great magic show !")

# Using range()
for value in range(1, 5):
    print(value)

# You can make a list using list(). This is convenient when having a large list of numbers
numbers = list(range(1, 6))
print(numbers)

# making list of even numbers
even_numbers = list(range(2, 20, 2))
print(even_numbers)

# squared value
list1 = []
for value in range(1, 11):
    squared = value ** 2
    list1.append(squared)
print(list1)

# Easier method for squared value
list2 = []
for value in range(1, 11):
    list2.append(value ** 2)
print(list2)

# min , max ,sum
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# List comprehension - one line code, syntax -> descriptive_name = [expression (for loop)]
squared = [value ** 2 for value in range(1, 11)]
print(squared)

# Slicing a list
players = ['charles', 'baker', 'michael', 'eli']
print(players[1:2])
print(players[2:])
print(players[:2])

# Copying a list
copied_players = players[:]
print(copied_players)

# Tuples - immutable
dimensions = (200, 50)

