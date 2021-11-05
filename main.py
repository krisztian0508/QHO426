career = input("Should I become a front end developer or a back end developer?\n")
#verifying the condition
if career == "front end developer":
  company = input("Which company will be the gretest one to start with, IBM or Google?\n")
  #using "or" operator
  if company == "IBM" or "google" :
    print("This is a great company to start with!")
  else:
    print("I will do my best to be hired by this company!")
elif career == "back end developer":
   company_2 = input("Will be HP  a good company to start my career with?")
   if company_2 == "yes" :
    print("In this case I will look on the company website for a deep reaserch.")
   else:
    print("It is a good idea to do more reaserch!")
else:
  print("Perhaps I should think for something else!") 