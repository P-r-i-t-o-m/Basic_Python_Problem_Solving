```python
# Creating a dictionary
user = {
    "name": "my name",
    "age": 28,
    "email": "myemail@gmail.com",
    "is_verified": True
}

# Printing the dictionary
print(user)

# Accessing values using keys
print(user["name"])  # Outputs: my name
print(user["age"])   # Outputs: 28

# Accessing a non-existent key
print(user.get("password"))  # Outputs: None

# Accessing a key with get method
print(user.get("age"))  # Outputs: 28

# Modifying existing values
user["age"] = 29
print(user["age"])  # Outputs: 29

# Adding a new key-value pair
user["job"] = "teaching"
print(user)  # Outputs: Dictionary with the new key-value pair added
```