```python
# Define a tuple
number_tuple = (1, 2, 3)

# Traditional approach
add_number_tuple = number_tuple[0] + number_tuple[1] + number_tuple[2]
print(add_number_tuple)

# Assigning to variables
x, y, z = number_tuple
print(x + y + z)

# Python unpacking
a, b, c = number_tuple
print(a + b + c)

# Using a list
number_list = [1, 2, 3]
a, b, c = number_list
print(a + b + c)
```