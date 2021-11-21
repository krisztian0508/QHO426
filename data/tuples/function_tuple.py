#1st function
def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods), max(likelihoods)
#2nd function
def run():
  falling = likelihood()
  print(f"Minimum likelihood of falling: {falling[0]}%")
  print(f"Maximum likelihood of falling: {falling[1]}%")
  
#call the function
run()