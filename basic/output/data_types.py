name = input("What is your name human?\n")
name_cap = name.capitalize()
age = int(input("How old are you?\n"))
height = float(input("How tall are you?\n"))
weight = float(input("How many kg do you have?\n"))
#formula: bmi=weight(kg)/height**2 (m**2)
bmi = weight / height**2
bmi_last = round(bmi, 2)
bmi_last = "{:.2f}".format(bmi)
print(f"{name_cap} you are {age} years old and your bmi is {bmi_last}.")