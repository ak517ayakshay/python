# as python didnt have switch case match case was introduced to it from version 10 and case _ is used as default so if u r in interview this is best way to check weather u r updated or not
while(1):
    c= int(input("enter the choice 1-+ 2-- 3-/"))
    match c:
        case 1:
            a=int(input("enter two numbers"))
            b=int(input())
            print(a+b)
        case 2:
            a=int(input("enter two numbers"))
            b=int(input())
            print(a-b)
        case 3:
            a=int(input("enter two numbers"))
            b=int(input())
            if(b!=0):
                print(a/b)
            else:
                print("divide by exception")
        case _ if ( c>=1000000  ) :
            #u can also add if conditions in this case with _
            print("lol its a joke")        
        case _:
            #case _ is used as default case always
            print("invalid choice")                
