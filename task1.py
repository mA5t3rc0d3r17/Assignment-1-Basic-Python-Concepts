# Get input from user for two numbers
first = input("Enter the first number: ")
second = input("Enter the second number: ")

# Convert the input strings to integers
first = int(first)
second = int(second)

# Perform arithmetic operations
add = first + second        # Addition
subt = first - second       # Subtraction
mult = first * second       # Multiplication
div = first / second        # Division

# Print a blank line for better readability
print("\n")

# Display the results of all operations
print("Addition: ", add)
print("Subtraction: ", subt)
print("Multiplication: ", mult)
print("Division: ", div)