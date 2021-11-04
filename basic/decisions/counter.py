first_number = int(input("Please enter the first whole number:\n"))
second_number = int(input("Please enter the second whole number:\n"))
third_number = int(input("Please enter the third whole number:\n"))
list =[first_number, second_number,third_number]
even_count, odd_count = 0, 0

for num in list:
      
    # checking condition
    if num % 2 == 0:
        even_count += 1
  
    else:
        odd_count += 1
print(f"There were {even_count} even and {odd_count} odd numbers. ") 
print() 
print("Beep is learning mathematical operators quite fast!")      