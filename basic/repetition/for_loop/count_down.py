# ask users fow far we have until we reach the cave
distance = int(input("How far are we from the cave?\n"))

#space
print()

# Display count down
#distance = distance we gonna reach the cave(strating point), "0" when we reach the cave(ending point), with how many steps in this case before to reach the cave and "-1", how to count the backwards steps
for count in range(distance, 0, -1):
    print(count, "steps remaining")

print("We have reached the cave!")