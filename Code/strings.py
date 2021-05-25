course1 = "Python's Course for Beginners"
print(course1)
course2 = 'Python for "Beginners"'
print(course2)
course3 = '''
Hi John,

Here is our first email to you.

Thank you,
The support team 
'''

print(course3)

print(course2[0])
print(course2[-1])
print(course1[0:3]) # return characters starting from index 0 to index 2 , excluding index 3
print(course1[0:]) # will output the whole string
print(course1[:]) # will output entire string

name = 'Jennifer'
print(name[1:-1])