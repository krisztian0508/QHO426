# Ask user for number
sum = int(input("How many numbers should I sum up?\n"))

# Declare a control variable
summed = 0

#space between rows
print()

# Sum numbers
total = 0

while (summed < sum):
    print("Please enter number", summed, "of", sum, ":")
    number = int(input())
    total += number
    summed += 1

# Display result
print("The answer is", total)