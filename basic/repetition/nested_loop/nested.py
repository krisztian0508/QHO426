#ask user about rows
rows = int(input("How many rows should I have?\n"))
#ask user about columns
columns = int(input("How many columns should I have?\n"))

# Display grid
for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(":-)", end="")
    print() 