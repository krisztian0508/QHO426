lives = int(input("Please enter the number of lives.\n"))
energy_level = int(input("Please enter the energy level.\n"))
shield_level = int(input("Please enter the shield level.\n"))

print("Health has been set.")

print(f"Lives:  {'♥' * lives}")
print(f"Energy: {'♦' * energy_level}")
print(f"Shield: {'♦' * shield_level}")