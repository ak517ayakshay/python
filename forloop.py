#for loop for strings
name="akshay the great"
for i in name:#this is the way it auto itarates to next element
    print(i)
    if(i==" "):
        print("completion of 1 word")
#for loop for lists
lists=["akshay","sudhanva","ayush","aarnav"]
for i in lists:
    print(i)
    for j in i:
        print(j)
for k in range(5):
    print(k) 
# this prints from 0 to 5
# if u want both starting and ending point u can give it
for j in range(9,14):
    print(j)
#if u want to increment number by x mention it in box
for k in range(1,7,2):
    # this by 2
    print(k)
