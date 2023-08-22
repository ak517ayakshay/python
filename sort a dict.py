a={
}
b=int(input("enter no of candidates"))
for i in range(b):
    c=input("enter student name")
    d=int(input("enter marks"))
    a[c]=d
print(a)
s=(sorted(a.items(),key=lambda x:x[1]))
# this is the way to sort the dictionary we need to use the sorted function to do it first argu accepts all the values to compare and second we need to use lamda function so that it should compare as tuples and x:x[1] indicates we r selecting coloum 1 that is 0,1 in the dict to sort this sorts the dict we externally need to use dict func to convert back to dict as it sorted func returns in list 
# ****** when u put 0 in x:x[0] it sorts based on the keys and if u put 1 it sorts based on values/item
print(s)
print(type(s))
