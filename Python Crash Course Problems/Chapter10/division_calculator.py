# print(5/0)  # Will give a Traceback error
# When returning the error, ZeroDivisionError is an exception object
# We can use this information to modify the program, such that if it happens again, we're prepared.

print("Give me two numbers to divide.")
print("Enter 'q' to quit.")
while True:
    num1 = input("\nFirst number: ")
    if num1 == 'q':
        break
    num2 = input("\nSecond number: ")
    if num2 == 'q':
        break
    try:
        answer = int(num1) / int(num2)
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by Zero!")