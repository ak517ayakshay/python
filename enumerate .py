# it is enum function it is used to get the index of particular element
j=[2,3,4,5,6,7,8,9]
for i,r in enumerate(j):
    if(i==3):
        print("i am at 3rd posi")
    print(r)    
# when u do this it automatically gets the index of the element and no need of temp variable and then incrementing it
#............
str1="akshay"
for r in enumerate(str1):
    print(r,type(r))
# when u do it for strings and use single variable r it acts as tuple and stores both index and the value at the index when u use i,r tuple gets unpacked
for i,r in enumerate(j,start=3):
    if(i==3):
        print("i am at 3rd posi")
    print(r)   
    # this starts from 3rd posi