```python
# Creating a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Printing the 2D list
print(matrix)

# Accessing elements
print(matrix[0])  # First row
print(matrix[1])  # Second row
print(matrix[2])  # Third row
print(matrix[0][2])  # Element at row 0, column 2
print(matrix[1][1])  # Element at row 1, column 1

# Modifying a value
matrix[0][2] = 15
print(matrix)

# Using nested for loops to print each item
for row in matrix:
    for item in row:
        print(item)
```