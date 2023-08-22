a={
}
b=int(input("enter no of candidates"))
for i in range(b):
    c=input("enter student name")
    d=int(input("enter marks"))
    a[c]=d
print(a)
s=dict(sorted(a.items(),key=lambda x:x[1]))
c=b+1
print("name\t\tmarks\t\trank")
for k in s:
    c=c-1    
    print(f"{k}\t\t{s[k]}\t\t{c}")