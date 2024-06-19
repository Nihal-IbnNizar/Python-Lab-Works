#JSON to Pyhton

import json
x = '{"name":"Nihal","age":23,"city":"Kannur"}'

y = json.loads(x)
print(y["age"])


#Python to JSON

x = {
    "name":"Anshad",
    "age":23,
    "city":"Wayanad"
}

y = json.dumps(x)
print(y)
print(type(y))