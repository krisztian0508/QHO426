'''import matplotlib.pyplot as plt

def read_data(file_path):
  temps = []
  with open(file_path) as file:
    for line in file:
      temps.append(float(line.strip()))
  return temps

def run():
  data = read_data('/User/czgone/PycharmProjects/HQO426/temps.txt')
  fig, (ax1, ax2) = plt.subplots(1, 2)
  ax1.plot(range(len(data)), data)
  ax2.bar(range(len(data)), data)
  plt.show()

run()'''

'''
import matplotlib.pyplot as plt
import random as rnd

def data():
  paths = {}
  
  line_style = input("What type of marker (o, s or ^)?\n")
  colour = input("What colour (r, g or b)?\n")
  marker_style = input("What type of marker (o, s or ^)?\n")
  
  paths['line_style'] = line_style
  paths['colour'] = colour
  paths['marker_style'] = marker_style
  
  return paths
  
def generate():
  num_lines = int(input("How many lines would you like to display?\n"))
  
  for num_line in range(num_lines):
    values = data()
    x = rnd.sample(range(1, 10), 5)
    y = rnd.sample(range(1, 10), 5)
    format = f"{values['colour']}{values['line_style']}{values['marker_style']}"
    plt.plot(x, y, format)
  
  plt.show()


def run():
  print("Running...")
  generate()
  print("Done!")
  
run()'''
'''
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(frame):
  print(f'Frame: {frame}')

def run():
  fig, ax = plt.subplots()
  simple_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)
  plt.show()

run()
'''
import matplotlib.pyplot as plt   
import matplotlib.animation as animation
     
fig, ax = plt.subplots()
    
def animate(frame): 
  # your code here 
  print(f'Frame: {frame}')
def run():
  global fig  
  # your code here (use fig with animation function)
  fig, ax = plt.subplots()
  simple_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)
  plt.show()

run()