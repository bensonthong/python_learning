# for x in range(4):
#     for y in range (3):
#         print(f"({x}, {y})")

# goes through x first loop then does all the inner loop counters ...

numbers = [5, 2, 5, 2, 2]

# for val in numbers:
#     print('x'* val)


# Using nested loops

for x in numbers:
    output = ""
    for y in range(x):
        output += 'x'
    print(output)