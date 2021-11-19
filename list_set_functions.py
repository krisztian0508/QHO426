def fruits():
  mylist = []
  fruits_list = ["apple", "banana", "kiwi", "orange", "melon"]
  for x in range(5):
    f = input("Here you can add a fruit of your choise:\n")
    for y in fruits_list:
      if f == y:
         mylist.append(f)
  return mylist
def run():
  print(fruits())
run()      
