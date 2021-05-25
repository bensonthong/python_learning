
# My answer
# price_house = 1000000
# is_good_credit = input("Do you have a good credit or bad credit? ")
# check_bool = bool(is_good_credit)
#
# if check_bool:
#     price_house *= 0.10
#     print(price_house)
# else:
#     price_house *= 0.20
#     print(price_house)

# Solution
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")