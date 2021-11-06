# Ask user for number
numbers_to_sum = int(input("How many numbers should I sum up?\n"))

# Declare a control variable
summed = 0

# space bewtween rows
print()

# Sum numbers
total = 0

while (summed < numbers_to_sum):
    print("Please enter number", summed, "of", numbers_to_sum, ":")
    number = int(input())
    total += number
    summed += 1

#result
print("The answer is", total, "!")