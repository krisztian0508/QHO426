#1st function
def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions
#2nd function  
def menu():
  print()
  print("Please select a direction:\n")
  print()
  dirs = directions()
  for index in range(len(dirs)):
    print(f"{index}: {dirs[index]}")
#3rd function
def run():
  menu()
#call the function
run()