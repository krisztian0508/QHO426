# ask user what to do
first_ask = input("Where should I look?\n")    
if first_ask == "in the bedroom":
    second_ask = input("Where in the bedroom should I look?\n")
    if second_ask == "under the bed":
        print("Found some shoes but no battery!")
    else:
        print("Found some mess but no battery.")
elif first_ask == "in the bathroom":
    second_ask = input("Where in the bathroom should I look?\n")
    if second_ask == "in the bathtub":
        print("Found a rubber duck but no battery!")
    else:
        print("Found a wet surface but no battery.")
    
elif first_ask == "in the lab":
    second_ask = input("Where in the lab should I look?\n")
    if second_ask == "on the table":
        print("Yes! I found my battery!!")
    else:
        print("Found some tools but no battery.")
else:
  print("I do not know where that is but I will keep looking.")

