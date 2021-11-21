def short_pattern():
  pattern = {"sequence":"101", 
  "occurrences": 5}
  return pattern
def medium_pattern():
  pattern = {"sequence":"111000", "occurrences": 25}
  return pattern
def long_pattern():
  pattern ={"sequence":"1100110011001100", "occurrences":50}
def run():
  print("Analysing patterns...")
  last_dic = {"short sequence": short_pattern, "medium sequence": medium_pattern, "long sequence": long_pattern}

run()  