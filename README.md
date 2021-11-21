import basics.functions.function_calls as function_calls
import basics.functions.multiple_functions as multiple_functions

def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run")
    response = input()
    if (response == "function_calls"):
        function_calls.run()
    elif (response == "multiple_functions"):
        multiple_functions.run()


def run():
    is_running = True

    while(is_running):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")

run()