person = {"name": "yisehak", "grade": 12} # a variable is specified in a list
for key, value in person.items():
print(f"[key]: [value]")

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 25

# Adding a new key-value pair
person["job"] = "Engineer"

# Updating a value
person["age"] = 26

# Removing a key-value pair
del person["city"]

# Printing the updated dictionary
print(person)
