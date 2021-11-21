#first function
def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight
#second function
def calc_avg_weight(beep_weight, bop_weight):
    average_weight = (beep_weight + bop_weight) / 2
    return average_weight

def run():
    # retrieve required user data
    beep_weight = float(input("What is the weight of Bop?\n"))
    bop_weight = float(input("What is the weight of Beep?\n"))

    user_choise = input("What would you like to calculate: sum or average?\n")

    # determine and carry out action
    if (user_choise == "sum"):
        result = sum_weights(beep_weight, bop_weight)
        #2 digits after the whole number
        print("The sum of Beep and Bop's weight is {:.2f}".format(result))
    elif (user_choise == "average"):
        result = calc_avg_weight(beep_weight, bop_weight)
        print("The average weight of Beep and Bop is {:.2f}".format(result))
    else:
        print("I am not sure what you would like to do.")
run()  