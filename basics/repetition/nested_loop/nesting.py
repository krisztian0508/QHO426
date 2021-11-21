# Ask user for sequence and marker
sequence = input("Please enter a sequence:\n")
marker = input("Please enter the character for the marker:\n")

# Find markers
marker1_position = -1
marker2_position = -1

for position in range(0, len(sequence), 1):
    letter = sequence[position]

    if (letter == marker):
        if (marker1_position == -1):
            marker1_position = position
        else:
            marker2_position = position

# Display result
print(f"The distance between the markers is {marker2_position - marker1_position - 1}.")
