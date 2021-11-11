def display_ladder(steps):
    # Display each step 
    for step in range(steps):
        print("| |")
        print("***") 
    
def create_ladder():
    steps = int(input("How many steps remain?\n"))
    display_ladder(steps)
#call function
create_ladder()