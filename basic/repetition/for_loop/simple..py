# Ask user for number of mountains 
mountains = int(input("How many mountains should I display?\n"))

# message letting the user know the command is loading..
print("\nDisplaying...")

#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. In our case "mountains"(typed by the user) var will give the number the sequence will be repeted 
for mountain in range(mountains):
  print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\


     """)
print("Done!")


           
       
        
      
     


