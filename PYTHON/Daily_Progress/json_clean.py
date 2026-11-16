"""import json
import pandas as pd
data = json.loads('{"name": "John", "age": 30, "city": "New York"}')
ab = pd.json_normalize(data)
print(data)
#print(ab)  

import json

d = {'id': '09', 'name': 'Nitin', 'department': 'Finance'}
print("This is Python", type(d))

print("Now Convert from Python to JSON")
obj = json.dumps(d, indent=4)
print("Converted to JSON", type(obj))
print(obj) """

import json

# --- DESERIALIZATION: JSON String to Python Dict ---
json_string = '{"name": "Alice", "age": 30, "is_admin": true, "hobbies": ["reading", "cycling"]}'

# json.loads() parses the string
user_data = json.loads(json_string) 

print(user_data)  # Output: {'name': 'Alice', 'age': 30, 'is_admin': True, 'hobbies': ['reading', 'cycling']}
print(type(user_data))  # Output: <class 'dict'>
print(user_data["name"])  # Output: Alice

# --- SERIALIZATION: Python Dict to JSON String ---
python_dict = {
    "product": "Laptop",
    "price": 999.99,
    "in_stock": True,
    "features": None
}

# json.dumps() converts the dict to a string
new_json_string = json.dumps(python_dict, indent=4) 
print(new_json_string)
