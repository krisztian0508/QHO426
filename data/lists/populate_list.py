#1st function
def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions
#2nd function
def menu():
  print("Please select a direction:")
  dirs = directions()
  for index in range(len(dirs)):
    print("{}: {}".format(index, dirs[index]))
  #create a var to store user indication  
  index = int(input())
  return dirs[index]
#3rd function
def run():
  route = []
  print("Working out escape route...")
  for count in range(4):
    route.append(menu())
  print(f"Escape route: {route}")
#call function
run() 