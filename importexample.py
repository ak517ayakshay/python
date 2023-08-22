def intro():
    print("this is used to show tht u can create 2 directories and import from each other")

# there may be some statements which should be executed only when u run this program and shld not be executed when u call this instant to other directory
print("k")
if __name__=="__main__":
    print("i will be executed only if this program is executed i wont if it is called by another instant ")
    intro()

    # this executes agar isko yahe pe run kiya jaa raha hai agar dusri jaga se call karre import ki madad se toh ye nai karega

print(__name__)
