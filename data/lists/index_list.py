#first function
def movements():
  #creating a list with str and int 
   path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1 ]
   return path

def run():
  #space
  print()
  print("Moving...")
  #store the return list in a local variable 
  path = movements()
  #path 0 is first index in our list "Move Forward", in programing we start counting from 0
  #using f-string to combine int with str in this case;
  #using {} brackets to put inside our list and [] brackets for index
  print(f"{path[0]} for {path[1]} steps")
  print(f"{path[2]} for {path[3]} steps")
  print(f"{path[4]} for {path[5]} steps")
  print(f"{path[6]} for {path[7]} step")
#call the function
run()    