# Chapter 8 Functions

def greet_user(username):
    print(f"Hello {username}!")


def describe_pet(animal_type, pet_name):
    print(f"\nI have  a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


greet_user('Benson')
describe_pet('dog', 'bob')

# Keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')


# Default Values
# def describe_pet(pet_name, animal_type='dog'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#     describe_pet(pet_name='willie')

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# Optional Argument
def get_formatted_name(first_name, last_name, middle_name=''):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


print(get_formatted_name('bob', 'drake'))


# Returning a dictionary
def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


# Functions with list
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


list_names = ['john', 'jane', 'mary']
greet_users(list_names)

# Note any changes made to a list are permanent


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nFollowing models are printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a Function from Modifying a List
# To do this , you want to pass a copy of a list to a function such that any changes to the function will not be affected
# Example, function_name(list_name[:])

# Passing an Arbitrary Number of Arguments


def make_pizza(*toppings):
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'onions', 'extra cheese')

# When making a function that accepts multiple parameters and it happens
# that it has an arbitrary argument, put the arbitrary argument in the
# end on the function argument
# Ex. def make_pizza(size, *toppings):

# Arbitrary arguments can be used in


def build_profile(first, last, **user_info):  # The double asterisk causes Python to create an empty dictionary called user_info
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('benson', 't', location='cpp')
print(user_profile)


