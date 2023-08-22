list1=["akshay","legend","aky",1,True]
print(list1[0],list1[1],list1[3])
a=[1,11,99,8]
print(type(a))
# negative indexing = len - posetive index
# amd vice versa
if "akshay" in list1:
    # this is used to check weather item is in list
    print("yes")
else:
    print("no")  
if 1 in list1:
    print("y") 
# same thing u can do in string too
if "aks" in "akshay":
    print("t")

print(list1[1:3])
# this prints from index 1 to 3 (slicing)
print(list1[0:4:2])
# last 1 is jump index if its 2 the alternate values r printed called as slicing

# creating ready made lists
aky= [i for i in range(5)]
print(aky)

aa=[i*i for i in range(5)]
print(aa)
# u can also write a condition
a=[i for i in range(4) if i % 2==0]
print(a)
aa=[i for i in range(10) if i % 3==0]
print(aa)
