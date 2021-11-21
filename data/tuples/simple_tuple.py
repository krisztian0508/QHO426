#1st function
def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods)
 
#2nd function
def run():
  print()
  #min value is 4
  print(f"Minimum likelihood of falling: {likelihood()}%.")

#calling the function
run()