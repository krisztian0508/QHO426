#import modules 
#before i put both of the modules in a function called run 
#def run():
  #print("System Failure Imminent!")
import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
#i defined another function to run what the user will chose to run
def run_block_a():
    response = input("Which program in 'Block A: Basics' do you wish to run: simple message or multiline message?\n")
    if (response == "simple message"):
      #if the ansewer is "simple message" then the program will run first module imported from simple_messsage, file saved in first week
        simple_message.run()
        #add space 
        print()
    elif (response == "multiline message"):
        multiline_message.run()
        print()

#i choose a boolean value for my function and also i put a condition to ask the user when my function is running , what would the user like to do
print()
def run():
    is_running = True

    while(is_running):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()
#Condition to run block a or quit the programa
        if (response == "a"):
            run_block_a()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")
#i called the function
run()