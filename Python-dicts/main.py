# working with dictionaries (key values pairs)

# Example 1
person = {
    'name': 'John',
    'age': 23,
    'sex': 'male',
    'grade': 3,
}

# Loop through the dictionary
for key, value in person.items():
    print(key, value)


# Accessing the dictionary
print(person['name'])
person['year'] = 2024
person['name'] = 'vinald'
print(person)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)


# Example 2
months = {
    'jan': 'january',
    'feb': 'february',
    'march': 'march',
    'apr': 'april',
    'may': 'may',
    'jun': 'june',
    'jul': 'july',
    'aug': 'august',
    'sept': 'september',
    'oct': 'october',
    'nov': 'november',
}


print(months)

# Accessing the dictionary
print(months['jan'])
print(months.get('samuel'))

# Printing the keys
print(months.keys())

# Printing the values
print(months.values())

# Printing the items (key value pairs)
print(months.items())

# Adding a new key value pair
months.update({'dec': 'december'})

# Loop through the dictionary
for key, value in months.items():
    print(key, value)