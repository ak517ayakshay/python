def convert(*n):
    b=tuple(n)
    print(type(b))

a=int(input("enter no of terms u need to add"))
b=[]
for i in range(a):
    o=int(input("enter"))
    b.append(o)
print(type(b))    
c=int(input("do u want to convert it to tuple press 1"))
if(c==1):
    convert(b)
else:
    print("thank u for using me")    

