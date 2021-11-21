print("\tWelcome to the tip calculator!")
print()
bill = float(input("What was the total bill?\n"))


tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))

people = int(input("How many people to split the bill?\n"))

bill_tip = float(tip/100 * bill + bill)
#pentru a avea intotdeauna doua decimale atunci formatam 
bill_tip_last = round(bill_tip, 2)
bill_tip_last = "{:.2f}".format(bill_tip)

bill_per_person = bill_tip_last / people
final_amount = round(bill_per_person, 2)
#pentru a avea intotdeauna doua decimale atunci formatam 
final_amount = "{:.2f}".format(bill_per_person)

print(f"In this case the total bill will be {bill_tip_last}£, meaning {final_amount}£ per person.")