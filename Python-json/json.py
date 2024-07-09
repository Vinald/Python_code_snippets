import json


# Python object
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Convert Python object to JSON
json_data = json.dumps(data)


# Save JSON data to a file
with open('output.json', 'w') as file:
    json.dump(data, file)


# read the json file and convert it to a python object
with open('output.json', 'r') as file:
    data = json.load(file)
    print(data)
    print(type(data))


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

User('Mj', 23)


# Convert Python object to JSON
def encode_user(object):
    if isinstance(object, User):
        return {'name': object.name,
                'age': object.age,
                object.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')
