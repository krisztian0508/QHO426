# Declare a control variable
cables_avoided = 0
#give a short var
i = cables_avoided
# ask user how many cables to avoid
cables_to_avoid = int(input("How many live cables should I avoid?\n"))

#give a short var for cables_to_avoid
j = cables_to_avoid

#Space between rows
print()

# how function while helps to avoid cables
while i < j:
  i += 1
  print("Avoiding...Done!", i, "live cables avoided.")
print()  
print("All live cables have been avoided.")  

#another way to solve this problem
''' # Declare a control variable

cables_avoided = 0

# ask user how many cables to avoid

cables_to_avoid = int(input("How many live cables should I avoid?\n"))

#Space between rows
print()

# how function while helps to avoid cables
while (cables_avoided < cables_to_avoid):
  cables_avoided += 1
  print("Avoiding...Done!", cables_avoided, "live cables avoided.")
  
#space  
print()  
print("All live cables have been avoided.") '''