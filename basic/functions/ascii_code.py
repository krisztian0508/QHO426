print("\nProgram Started!\n")
character = input("Please enter a standard character:\n")

if (len(character) == 1):
    print("The ASCII code for {} is {}".format(character, ord(character)))
else:
    print("A single character was expected.")

print("Program Ended!")