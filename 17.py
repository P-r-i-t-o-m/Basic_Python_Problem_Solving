```python
# Define a list of grocery items
grocery_list = ['egg', 'rice', 'bread', 'sugar']
print(grocery_list)

# Access elements using index
print(grocery_list[0])  # egg
print(grocery_list[1])  # rice
print(grocery_list[-1]) # sugar
print(grocery_list[-2]) # bread

# Slice the list
print(grocery_list[2:])   # ['bread', 'sugar']
print(grocery_list[:2])   # ['egg', 'rice']
print(grocery_list[1:2])  # ['rice']

# Modify an item in the list
grocery_list[1] = 'oil'
print(grocery_list)      # ['egg', 'oil', 'bread', 'sugar']

# Working with numeric lists
price = [10, 5, 8, 15, 3]
max_price = price[0]

for value in price:
    if value > max_price:
        max_price = value

print(max_price)         # 15
```