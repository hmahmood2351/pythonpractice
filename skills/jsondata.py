import json
from pstats import SortKey 

person2 = {'name':'squid', 'age':22}
personJSON = json.dumps(person2, indent=4, sort_keys=True)

print(personJSON)

with open('sample2.json', 'r') as file:
    person = json.load(file)
    print(person)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
user = User('squid',22)

def encode_user(o):
    if isinstance(o, User):
        return {'name':o.name, 'age':o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name':o.name, 'age':o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJSON = UserEncoder().encode(user)
print(userJSON)

#decode (and encoding above) custom objects

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user), type(userJSON))
print(user.name)