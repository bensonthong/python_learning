# Chapter 6 Dictionaries- wrapped in curly braces {}, key-value pair. Python returns they value associated with the key.

# Example
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print("===================================================")
# adding a key-value pair in Dictionary
alien_0['x_position'] = 2
print(alien_0)
print("===================================================")
# Can added key-value pair on an empty dictionary
alien_1 = {}
alien_1['color'] = 'purple'
alien_1['point'] = 1
print(alien_1)
print("===================================================")
# Example of moving an alien at different speed
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
print("===================================================")

# Removing Key-Value Pairs
alien_3 = {'color': 'blue', 'points': 5}
print(alien_3)
del alien_3['points']
print(alien_3)
print("===================================================")

# Good notation to write dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# get() to access values- use only if not sure if key exist in the dictionary
alien_4 = {'point': 5}
# point_value1 = alien_4['points']
point_value1 = alien_4.get('points', 'No point assigned')      # Compiler will output 'No point assigned' because they key value pair is spelled wrong
print(point_value1)
print("===================================================")
# Looping through a dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
