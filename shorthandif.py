a=int(input("no1"))
b=int(input("no2"))
print(a) if a>b else print("=") if a==b else print(b)
# this is like readable english shorthand if is such 
# if u have ntg to print after else 
print(a) if a>b else " "
# this is must u shld write ""  and even else orelse it will be a syntax error 
c=9 if a>b else 0
print(c)
# this is so readable