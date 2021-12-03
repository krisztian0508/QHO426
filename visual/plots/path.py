import matplotlib.pyplot as plt

def coordinate():
  x = int(input("You can add a value for X \n"))
  y = int(input("You can add a value for Y\n"))
  return(x, y)

def  path():
  print("Retrieving path...")
  x_values = []
  y_values = []
  for count in range(4):
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
  return[x_values, y_values]  

def run():
  values = path()
  plt.plot(values[0], values[1], 'c--s')
  plt.show()

run()  
  
#The function should then display a line plot using values[0] for the x values and values[1] for the y values. 
