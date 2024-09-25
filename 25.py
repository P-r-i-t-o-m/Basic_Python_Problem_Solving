```python
# Create the emoji dictionary
emoji_dict = {
    ':)': '😊',
    ':(': '😢'
}

# Take input from the user
message = input("Type your message: ")

# Split the message into words
separated_words = message.split()

# Initialize an empty output string
output = ""

# Convert words to emojis using the dictionary
for word in separated_words:
    output += emoji_dict.get(word, word) + " "

# Print the output
print(output)
```