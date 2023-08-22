names=input("enter names with spaces in between")
count=0
t=names.split(" ")
a=(input("enter  alpha"))
for i in t:
    for j in i:
        if(j==a):
            count=count+1
print(count)