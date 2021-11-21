import random

min_value = int(input("Please enter the minimum value:\n"))

max_value = int(input("Please enter the maximum value:\n"))

random_number = random.randrange(min_value, max_value)

print("I am thinking of a number between {} and {}.".format(min_value, max_value), "Can you guess what it is?")


guess = 0

while(guess != random_number):
  guess = int(input("Please enter a number:\n"))

  if (guess == random_number):
    break
  elif (guess < random_number):
    print("Your guess is too low.")
  else:
    print("Your guess is too high.")
  
print("Congratulations! You guessed my number!")