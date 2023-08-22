a=(input("enter"))
# didmt use int here as ::-1 reverses the string and not ints 
b=a[::-1]
if(a==b):
    print("palindrome")
else:
    print("nope")    