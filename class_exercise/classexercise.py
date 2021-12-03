import matplotlib.pyplot as plt

def triangule():
  x = [4, 7, 7,4]
  y = [4, 7, 4,4]
  plt.plot(x, y)
  #plt.show
def trapezium():
  x = [2, 3, 10, 11, 2]
  y = [2, 9, 9, 2, 2]
  plt.plot(x, y, 'g--s')
  #plt.show
def parallelogram():
  x = [1, 2, 14, 13, 1]
  y = [1, 11, 11, 1, 1]
  plt.plot(x, y, 'b-p')
  #plt.show
def run():
  triangule()
  trapezium()
  parallelogram()
  plt.show()
  
run()
