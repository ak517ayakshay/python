
a=(input("enter the no whose multipication table u want"))


try:
    for i in range(1,11):
     print(f"{int(a)}x{i}={int(a)*i}")  
except Exception as e:    
       print(e)       
print("thank u a")    

try:
    b=int(input("En") )
except:
    print("inavlid input")    
    # this is called as value error which is handeled here