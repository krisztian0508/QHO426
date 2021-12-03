import matplotlib.pyplot as plt
def display(x, y):
  plt.plot(x, y,'o')
  plt.show()

def run():
  x = [1, 2, 3, 4, 5]
  y = [1, 4, 9, 16, 25]
  #running the first func
  display(x, y)


'''We wish to create a program to display the path Beep and Bop are taking through Robo City.

The program should consist of the following two functions:

The first function should be named display and should take 2 parameters. 
The first parameter is a list of x values. 
The second parameter is a list of y values. 
The function should display a line plot using the arguments supplied for the parameters. 

The second function should be named run and should take 0 parameters. 
The function should create an empty list named x_values containing the following values: 1, 2, 3, 4, 5 
The function should then create an empty list named y_values containing the following values: 1, 4, 9, 16, 25 
The function should then call the first  function passing x_values and y_values as arguments. '''
