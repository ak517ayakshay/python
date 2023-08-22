for i in range(5):
    print(i)
else:
    print("i am completed")    
# VVIP
for i in range(6):
    print(i)
    if(i==3):
        break
else:
    print("i am complete")    
# here the else part doesnt get executed as the loops condition doesnt go false else is not executed when the loop is broken
# same thing happens even with while loop