import os
# Chapter 10 - Files and Exception
file = 'text_files/pi_digits.txt'
# open() - opens a file and returns an object representing the file called file_object
# with closes the file once it accesses the file
with open(file) as file_object:
    contents = file_object.read()       # read() reads the contents of file and store it as one long string
print(contents)

# This line of code checks to see if we are opening a file and will assert an error if opening a path(folder)
# path = r"text_files/pi_digits.txt"
# assert os.path.isfile(path)
# with open(path) as f:
#     pass

# Working with a File's Contents
# with open(file) as file_object:
#     lines = file_object.readlines()        # reading in lines
#
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))

# Check if your birthday appears in the one million digits of pi
file_name = 'text_files/one-million.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in mmddyy:")
if birthday in pi_string:
    print("Your birthday is in the million of digits of pi!")
else:
    print("Your birthday does not appear... :( ")

