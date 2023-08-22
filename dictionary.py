dic={
    "akshay":"legend",
    "aarnav" : "ytber"
}
print(dic)
# this is like mapping if u want to access legend u can do it using akshay
# print(dic[0]) u cant access it like this u need a key word to access it
print(dic["akshay"])
dic={
    "akshay":99 ,
    "sudhanva":90,
    "ayush":99
}
print("enter")
a=input()
print(dic[a])
# this gives me 99
# they r ordered collections
# there r 2 ways to call it
# 1)print(dic[a])
# 2)print(dic.get(a))
# these r like remove and discard func 1st one throws error if the element is not present while second one doesnt throw any sort of error

print(dic.keys())
# this shows all the keys in the dictionary
print(dic.values())
# this shows all the values in dict
# u can also itreat
for k in dic.keys():
    print(f"{k} has scored {dic[k]}")

#to print in pairs
print(dic.items()) 
