#first function with the list
def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions
#2nd function calling the first one
def run():
  print(directions())
#calling the function
run()