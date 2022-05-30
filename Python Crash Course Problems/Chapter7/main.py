# message = input("Tell me something and i'll repeat it back: ")
# print(message)

# Numerical Input
# age = input("How old are you? ")
# age = int(age)
# print(f"You are {age} years old")

# While loop
# current_num = 1
# while current_num <= 5:
#     print(current_num)
#     current_num += 1

# Allow user to quit
# prompt = "\nTell me something and ill repeat:"
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# Flags
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# While loop with lists and dictionaries
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Filling a dictionary with user input
responses = {}
polling_active = True
while polling_active:
    name = input("What is your name: ")
    response = input("Which mountain would you like to climb someday: ")

    responses[name] = response

    repeat = input("What would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n --- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")