#n!=n(n-1)*(n-2)*(n-3)...3*2*1
# Ask user for a number
number = int(input("Please enter a number?\n"))

# Calculate factorial
count = 0
total = 1

while ( count < number ):
    count += 1
    total *= count

print("The factorial is", total)
