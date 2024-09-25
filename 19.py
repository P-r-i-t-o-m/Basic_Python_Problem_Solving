```python
# Creating a list
number_list = [1, 2, 5, 1, 10, 14]
print(number_list)

# Appending an element
number_list.append(20)
print(number_list)

# Inserting an element at a specific index
number_list.insert(1, 7)
print(number_list)

# Removing a specific element
number_list.remove(2)
print(number_list)

# Sorting the list
number_list.sort()
print(number_list)

# Reversing the list
number_list.reverse()
print(number_list)

# Checking if an element is in the list
print(1 in number_list)
print(12 in number_list)

# Counting occurrences of an element
print(number_list.count(1))

# Finding the index of an element
print(number_list.index(10))

# Copying the list
number_list2 = number_list.copy()
print(number_list)
print(number_list2)

# Popping the last element
number_list.pop()
print(number_list)

# Clearing the list
number_list.clear()
print(number_list)
```