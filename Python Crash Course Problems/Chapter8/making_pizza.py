# import pizza
# When importing a module and using a function within the module, you need to
# You need to call the module.function_name(...)
# You can also import a specific function in the module using:
# from module_name import function_name so from pizza import make_pizza
# This allows user to not use the dot notation when calling the function
# from pizza import make_pizza
# make_pizza(16, 'pepperoni')

# This allows giving the function an alias name
from pizza import make_pizza as mp
mp(16, 'pepperoni')

# Similarly you can give a module an alias
# import pizza as p

# Import all functions in a module
# from pizza import * , not recommended as it can conflict with existing function name
# in your project

# Function should have descriptive names, use lower case and underscores.
