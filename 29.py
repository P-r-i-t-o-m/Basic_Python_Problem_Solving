```python
# Celsius to Fahrenheit Converter with Exception Handling

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Try-Except block to handle exceptions
try:
    # Input from user
    celsius = int(input("Enter temperature in Celsius: "))
    
    # Check for zero division error
    if celsius == 0:
        raise ZeroDivisionError("Celsius cannot be zero")

    # Conversion and output
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Temperature in Fahrenheit: {fahrenheit}")

except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError as e:
    print(e)
```