#1st function
def steps():
  all_steps = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
  return all_steps
#2nd function
def run():
  all_steps = steps()
  # create 2 empty tuples to populate the tuple later if condtions are true
  good_steps = []
  bad_steps = []
  #put conditions
  for step in all_steps:
    if (step[1] >= 50):
      #add in the tuple if condition is true
      bad_steps.append(step)
    else:
      good_steps.append(step) 
#print len of the steps after conditions
  print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")
#call the function
run()