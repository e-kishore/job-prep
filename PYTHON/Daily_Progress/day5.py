import json

user_data = {
    "id": 101,
    "name": "Asha",
    "is_active": True,
    "skills": ["Python", "SQL"]
}


# Write Python dict directly to a file
with open("user.json", "w") as file:
    return_value = json.dump(user_data, file, indent=2)

print("Function return value:", return_value)
print(type(return_value))  # Output: <class 'NoneType'>