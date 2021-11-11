# Ask user for phrase
phrase = input("Please enter a phrase?\n")
#count how many characters (inclusiv space) the user will write
len(phrase)
# Declare a control variable
bops = 0
# space
print()
#for every single charater the user will type will be a "bop". I will use "while" function to get the solution
while (bops < len(phrase)):
    print("Bop ", end="")
    bops += 1

#without while
'''phrase = input("Please enter a phrase: ")
x = len(phrase)
print(x * " Bop")'''