# Ask user for brightness level
brightness_level = int(input("What level of brightness is required?\n"))

# Adjust brightness
print("\nAdjusting brightness...\n")

for brightness in range(2, brightness_level + 1, 2):
    print("Beep's brightness level:", "*" * brightness)
    print("Bop's brightness level:", "*" * brightness)
#space    
print()    
print("Adjustments complete!")