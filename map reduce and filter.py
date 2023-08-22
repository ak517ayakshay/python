# MAP
def cube(c):
    return c*c*c
print(cube(2))
l=[2,3,4]
print(map(cube,l))
# this prints the map object which can easily be converted to list 
print(list(map(cube,l)))
f=lambda x:x*x*x
print(list(map(f,l)))
# filter
def less(c):
    return c<4
# this returns true if value is less thn 4 else fals
l=[1,3,4,5,2]
print(list(filter(less,l)))
# less is a function whichb returns boolean values and that is applied to each term in list of true the term is put in new list / printed if false ignored this is beauty of filter
# this prints all the values which r less than 4
print(list(filter(lambda x:x<3,l)))
# REDUCE
# u need to always import reduce
import functools
# reduce is function of functools
from functools import reduce
l=[1,2,3,4,5]
# l=[3,3,4,5]
# l=[6,4,5]
# l=[10,5]
# l=[15]
def sss(x,y):
    return x+y
sum=reduce(sss,l)
print(sum)
def d(x,y):
    return x*x+y**2
summ=(reduce(d,l))
print(summ)



















