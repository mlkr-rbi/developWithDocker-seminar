# Print "Hello!"
print("Hello!")

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of numbers
total = sum(numbers)

# Save the sum to a file
with open("helloNumbers.txt", "w") as file:
    file.write(f"The sum of numbers is: {total}\n")

print("I just made a file.")