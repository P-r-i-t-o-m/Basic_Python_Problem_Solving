```python
class Keyboard:
    def definition(self):
        print("Keyboard is an input device")
    
    def number_of_keys(self):
        print("There are 101 keys")

# Creating an object of the class
my_keyboard = Keyboard()

# Calling methods on the object
my_keyboard.definition()       # Output: Keyboard is an input device
my_keyboard.number_of_keys()   # Output: There are 101 keys

# Setting and printing an attribute
my_keyboard.brand = "Logitech"
print(my_keyboard.brand)       # Output: Logitech

# Creating another object of the class
new_keyboard = Keyboard()
new_keyboard.definition()      # Output: Keyboard is an input device

# Attempting to print a non-existent attribute
# print(new_keyboard.brand)    # Raises an AttributeError

# Setting an attribute for the new object
new_keyboard.brand = "Dell"
print(new_keyboard.brand)      # Output: Dell
```