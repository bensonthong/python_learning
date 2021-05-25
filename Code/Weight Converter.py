# weight = input("Weight: ")
# ask = input("(L)bs or (K)g: ")
#
# if ask == 'L'or ask == 'l':
#     kg = int(weight) * 0.453592
#     print(f'{kg} kg')
#
# elif ask == 'K' or ask == 'k':
#     lbs = int(weight) * 2.2
#     print(f'{lbs} lbs')


# Solution
weight = int(input('Weight: '))
unit = input('(L)bs or K(g)')
print(unit.upper)
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f'You are {converted} kilos')
else:
    converted = weight / 0.45
    print(f' You are {converted} pounds ')


