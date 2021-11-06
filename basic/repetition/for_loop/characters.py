# Ask user for markings
print("What strange markings do you see?")
markings = input()

# Identify markings
# a word between "\n" has an empty row up and an empty row down
print("\nIdentifying...\n")

for count in range(0, len(markings), 1):
    print("index", count, ":", markings[count])
  