```python
# Define a function to calculate the total cost
def total_cost(price, shipping, discount):
    total = price + shipping - discount
    print(f"Total cost: {total}")

# Call the function with different arguments
total_cost(10, 5, 1)   # Output: Total cost: 14
total_cost(20, 5, 5)   # Output: Total cost: 20
total_cost(40, 10, 1)  # Output: Total cost: 49

# Define a function with keyword arguments
def welcome(name):
    print(f"Hi {name}")

# Call the function with positional arguments
welcome("Nurgeomon Varikey")  # Output: Hi Nurgeomon Varikey

# Define a function to handle first and last names
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")

# Call the function with positional arguments
greet("Nurgeomon", "Faraki")  # Output: Hi Nurgeomon Faraki
```