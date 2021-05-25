course = 'Python for Beginners'
print(len(course)) # len and print are general purpose functions
print(course.upper()) #creates a new string and returns it capitalize, . operator is method(not a function)
print(course) # the upper does not modifying original string course
print(course.lower())
print(course.find('o')) #print the index of the parameter inside .find()

# if find something that does not exist in the string, then it outputs -1
# if find a word in the string such as Beginners, then it will output the index of the first letter of the word
# remember that a 'space' counts as an index

print(course.find(' '))

print(course.replace('Beginners','Absolute Beginners'))
# replace is case sensitive, if put something in old that dne then it won't replace


# This expression produces a boolean value/ aka boolean expression
print('Python' in course)

# difference between .find and the in, is that they have different outputs respectively. .find outputs the index, and in outputs a boolean value

# Results
# len() - prints the number of characters in a string (general purpose function)

# Methods
# course.upper()
# course.lower()
# course.title()
# course.find()
# course.replace()
# '...'  in (name of string)






