# for item in range(5,10,2):  # range outputs an object, not a list , paraamters: (range1,range2,step)
#     print(item)

prices = [10,20,30]
cost = 0
# item is a loop variable
for item in prices:
    cost += item
print(f"Total: ${cost}")