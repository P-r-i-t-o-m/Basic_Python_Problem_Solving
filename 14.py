```python
# Guessing Game using While Loop

# Set the actual price of the product
actual_price = 10

# Initialize guess_count and guess_limit
guess_count = 0
guess_limit = 5

# Start the while loop
while guess_count < guess_limit:
    # Get user input and convert it to an integer
    guess = int(input("Guess the price: "))
    
    # Check if the guess is correct
    if guess == actual_price:
        print("You won!")
        break
    
    # Increment the guess count
    guess_count += 1

# After the while loop
else:
    print("You failed")
```