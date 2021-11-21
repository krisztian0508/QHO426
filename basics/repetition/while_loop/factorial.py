#n!=n(n-1)*(n-2)*(n-3)...3*2*1
# Ask user for a number
num = int(input("\nPlease enter a number?\n"))
 # Calculate factorial
factorial = 1
f = factorial #simplifying
i = 1
 
while i <= num:
  f *= i #f = f*i
  i = i + 1
 
print("The factorial is", num, " is ", f)