```python
def add(number_1, number_2):
    return number_1 + number_2

result = add(1, 2)
print(result)

# If you remove the return statement, the function looks like this:
def add(number_1, number_2):
    print(number_1 + number_2)

# Calling this will output None
add(1, 2)
```