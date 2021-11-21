# Declare a control variable
cables_removed = 0

# Ask user how many cables to remove
cables = int(input("How many cables should I remove?\n"))

# take action and remove how many cables user told you to remove
print()

while (cables_removed < cables):
    cables_removed += 1
    print("Removed cable.")
    #put the condition until the condition is going to be false and the function to stop running
   
'''cables_to_remove = int(input("\nHow many cables should I remove?\n"))
cables_removed = 0
i = cables_removed
j = cables_to_remove
print()
while i < j:
  i += 1
  print("Removed cable.")'''