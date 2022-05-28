# 2-1 Assign a message to a variable, and then print that message
message = "This is a message"
print(message)

# 2-2 Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message
message2 = "This is the third message"
print(message2)
message2 = "This is actually the second message!"
print(message2)
print("================================================")
# NOTE: Inside single or double quotes are considered a string

# Changing Case in String: .upper, .lower, .title
name = "Benson"
print(name.title())
print(name.upper())
print(name.lower())

# Concatenation. This is done using f-strings which f stands for format
first_name = "Benson"
last_name = "T."
full_name = f"{first_name} {last_name}"
print(full_name)
message3 = f"Greetings, {full_name}!"
print(message3)

# NOTE: f-strings before Python 3.6, needs to use "{} {}".format() method

print("================================================")

# 2-3
name = "Eric"
print(f"Hello {name}, would you like to learn Python today")

# 2-4
print(name.title())
print(name.upper())
print(name.lower())

# 2-5 & 2-6
author = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
print(f"{author} once said, \"{quote}\"")

# 2-7 Stripping Names, using these strip methods removes whitespaces on string.
name = "\tCaryn\n"
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())


