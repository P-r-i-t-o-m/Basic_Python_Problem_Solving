```python
# Keyboard class with constructor
class Keyboard:
    def __init__(self, language, connection):
        self.language = language
        self.connection = connection

# Creating a keyboard object
my_keyboard = Keyboard("English", "Wireless")
print(my_keyboard.language)  # Output: English
print(my_keyboard.connection)  # Output: Wireless

# AboutMe class with constructor
class AboutMe:
    def __init__(self, name, address, occupation):
        self.name = name
        self.address = address
        self.occupation = occupation

    def talk(self):
        print(f"My name is {self.name}. I'm from {self.address}.")
        print(f"I am a {self.occupation}.")

# Creating an object of AboutMe class
fairuki = AboutMe("Nirjaman Faruki", "Bangladesh", "Teacher")
fairuki.talk()
# Output:
# My name is Nirjaman Faruki. I'm from Bangladesh.
# I am a Teacher.
```