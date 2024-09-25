```python
# Example 1: Iterating over a string
string = "python"
for character in string:
    print(character)

# Example 2: Iterating over a list of items
grocery_list = ["egg", "rice", "oil"]
for item in grocery_list:
    print(item)

# Example 3: Iterating over a list of numbers
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Example 4: Using the range function
for number in range(10):
    print(number)

# Example 5: Using range with a starting point and step
for number in range(5, 10, 2):
    print(number)

# Example 6: Calculating the total bill
bills = [10, 30, 50, 10]
total = 0
for bill in bills:
    total += bill
print(f"Total bill: ${total}")
```