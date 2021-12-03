

"""def search(file_path):
  print("Searching...")
  with open(file_path) as file:
    for line in file.readlines():
      print(f"Looked in {line.strip()}")
  print("...Done!")

def run():
  search("locations.txt")

run()"""


'''import matplotlib.pyplot as plt
def display(x, y):
  plt.plot(x, y,'o')
  plt.show()

def run():
  x = [1, 2, 3, 4, 5]
  y = [1, 4, 9, 16, 25]
  #running the first func
  display(x, y)
run()'''

import matplotlib.pyplot as plt

def small():
  x = [3, 3, 4, 4, 3]
  y = [3, 4, 4, 3, 3]
  plt.plot(x, y, 'r:o')
  
def medium():
  x = [2, 2, 5, 5, 2]
  y = [2, 5, 5, 2, 2]
  plt.plot(x, y, 'c--s')
  
def large():
  x = [1, 1, 6, 6, 1]
  y = [1, 6, 6, 1, 1]
  plt.plot(x, y, 'y-p')
  
def run():
  small()
  medium()
  large()
  plt.show()
  
run()