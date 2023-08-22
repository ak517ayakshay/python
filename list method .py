b=[1,4,2,4,6,12,113,45,24]
b.append(8)
# this adds 8 to the list
b.sort()
print(b)
# this sorts elements in the list
c=b[::-1]
# sorted in descending order using this can also use b.reverse
print(c)
d=b.index(6)
# this gives the index of the number six if there r 2 occurences gives first
print(d)
e=b.count(4)
# this method is used to count the number in the parenthesis eg 4 occcured twice so 2 is o/p
print(e)
f=[1,2,3,4,5]
# m=f 
#  u cannot directly do this when u dorectly do this the memory location of array remains same so the copy of the list is not given to m , rather m is just a refrenxe of f(polymorphism like) this is like in case of pointer so if u change m f also changes to avoid this use "copy "  func
m=f.copy()
m[0]=0
print(m)
print(f)
g=[1,3,4,5,6,7,7]
g.insert(3,999)
# this is also like append but to specific posi 3 is posi 999 is value
print(g)
f.extend(g)
# this means extend f and add g probably like conjugateing the stringsS
print(f)
h = f+g
# this can also be done for concatinating