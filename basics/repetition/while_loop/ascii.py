# Declare a control variable
bars_charged = 0
i = bars_charged
# Ask user for number of bars
bars_to_charge = int(input("How many bars should be charged?\n"))
j = bars_to_charge
# Display charged bars
print()

while (i < j):
  i += 1
  print("Charging:"," " "█" " "  * i)
  print()
    
print() 

print("The battery is fully charged.")  

  