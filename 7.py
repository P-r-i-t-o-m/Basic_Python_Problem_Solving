course_name = "learn python programming"

# Calculate the number of characters
print(len(course_name))

# Convert to uppercase
print(course_name.upper())

# Convert to lowercase
print(course_name.lower())

# Find the index of a character
print(course_name.find('t'))
print(course_name.find('T'))  # Case sensitive

# Find the index of a substring
print(course_name.find('Python'))  # Case sensitive

# Replace a substring
print(course_name.replace('learn', 'master'))

# Check if a substring is in the string
print('python' in course_name)
print('Learn' in course_name)  # Case sensitive
print('learn' in course_name)  # Case sensitive
