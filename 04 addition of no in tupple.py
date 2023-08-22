def sum(*n):
    # The asterisk (*) in front of n is used to indicate that n is a special kind of parameter known as a "varargs" parameter or "variable-length argument" parameter. It allows you to pass any number of arguments to the function, and they will be collected into a tuple named n.
    sum1=0
    for i in n:
     
        sum1=sum1+i

    print(sum1)    
a=int(input("en")) 
b=[0]
for i in range(a):
    o=int(input("val"))
    b.append(o)
sum(*b)
#* HERE IS called as the unpacking operator this unpacks the values from tuple and pass them individuallyz