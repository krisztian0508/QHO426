# ask user what to do
book_cover = input("What type of cover does the book have, soft cover or hard cover?\n")
    
if book_cover == "soft cover":
    bound = input("Is the book perfect-bound?\n")
    if (bound == "yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")
print()    
print("Anyway, enjoy the book!")    

    