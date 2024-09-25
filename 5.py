# Defining a string
course_name = "learn python programming"
print(course_name)

# Using double quotes to handle apostrophes
course_name = "parakeet's python course"
print(course_name)

# Using single quotes to handle double quotes
course_name = 'learn python programming with "double quotes"'
print(course_name)

# Multi-line string
multi_line_string = """I am a noisy man.
Fairy Key.
This is my Python course and this is the best Python course available online."""
print(multi_line_string)

# Accessing characters by index
course_name = "learn python programming"
print(course_name[0])   # Output: l
print(course_name[1])   # Output: e
print(course_name[-1])  # Output: g
print(course_name[-2])  # Output: n

# Slicing strings
print(course_name[0:3])     # Output: lea
print(course_name[1:])      # Output: earn python programming
print(course_name[:7])      # Output: learn p
print(course_name[1:-1])    # Output: earn python programmin
