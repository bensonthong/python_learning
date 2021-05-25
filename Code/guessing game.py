# win_value = 9
# i = 0
# while i < 3:
#     guess = int(input("Guess: "))
#     if guess == 9:
#         print("You won!")
#         break
#     else:
#         print("Wrong!")
#         i += 1
#         if i == 3:
#             print("You lose")

# Solution
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed')
# the else part gets executed when guess_count is greater than or equal to 3
