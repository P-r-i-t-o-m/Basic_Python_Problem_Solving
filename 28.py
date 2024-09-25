```python
def emoji_converted(message):
    separated_words = message.split()
    emoji = {
        "happy": "😊",
        "sad": "😢"
    }
    output = ""
    for word in separated_words:
        output += emoji.get(word, word) + " "
    return output

message = input("Type your message: ")
result = emoji_converted(message)
print(result)
```