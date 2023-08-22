age=int(input("enter ur age"))
if age<18:
    #when u use colon it defines ur indentation just like ur {
    print("you are minor")
    print("case 1")
elif age==18:
    #this is ur else if elif in python = else if in c
    print("u can vote") 
    print("case 2")
else:
    print("naughtyyy")   
    #if u do this u will get an error beocz input is taken always as string and u cant compare string and int so u need to typec9ast   
age=int(input("enter ur age"))
