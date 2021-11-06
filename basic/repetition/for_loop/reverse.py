# Ask user for phrase
phrase = input("What phrase do you see?\n")

# Identify markings
print("\nReversing...\nThe phrase is: ", end="")

for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")
  