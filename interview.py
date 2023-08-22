name = "harry"
print(name.upper())
#strings are imutable(u cant change them when u do name.upper new string is given the old string is not modified) meaning it doesnt change ur previous change it creates new string and applies the change which is given by u
# ............
# strftime is a method which converts dates to string and later we can convert it to readable format by typecasting refer greetingprogram.py for more
#.............
#pls refer matchcase.py its imp
#..............
# 
# def sum(*n):
    # The asterisk (*) in front of n is used to indicate that n is a special kind of parameter known as a "varargs" parameter or "variable-length argument" parameter. It allows you to pass any number of arguments to the function, and they will be collected into a tuple named n.
# b=[2,3,4] or else can be appended too
    # sum(*b)
#* HERE IS called as the unpacking operator this unpacks the values from tuple and pass them individuallyz
#..........
#a=(input("enter"))
# didmt use int here as ::-1 reverses the string and not ints 
# b=a[::-1]
# if(a==b):
#     print("palindrome")
# else:
#     print("nope")    
#...............
# tuple can only be created with single elment when , is put to its list eg a = (1,)this is a tuple but if u dont put , complier treats it as int a = (1)
#.............
#def ca(c,*n):
    # here u should first take the argument c and then *n as *n accepts only keyword only argument 
    #..............
    # doc strings(refer file its very imp) __doc__
    #...................................
    
    # aky = {}
# when u declare like this it is considered as dictionary as syntax of dic and set is same to create an empty set u need to do this
# aky = set()
#........................
# the main diffrence between remove and discard in sets is remove func throws error if element is not present whereas discard func thorws an error
#......................
# refer to for loop with else
#...................
#finally word is bomb see it
#..............
#str1="akshay"
# for r in enumerate(str1):
#     print(r,type(r))
# when u do it for strings and use single variable r it acts as tuple and stores both index and the value at the index when u use i,r tuple gets unpacked
#......................
# if __name__=="__main__":
#     print("i will be executed only if this program is executed i wont if it is called by another instant ")
# this executes agar isko yahe pe run kiya jaa raha hai agar dusri jaga se call karre import ki madad se toh ye nai karega
# ..................
# a=3
# b=3
# print(a is b)
# print(a==b)
# both r true beocz in python once 3 is created it is created only once in memory location from there it is accssed each time so once u give a=3 memory location is created but when u give b = 3 2nd time same memory location is used so a and b are pointing towards same memory location ie y its true above insead of contants if we give strings,tuples,sets answer is true true  is identity operator and == is comparison operator
#.....
#  to access a private variable _classname__attricbutname this is called NAME NAMGLING IN PYTHON
#>..
# is it necessary to give self argument to create a method in class
# ans is no eg static methods
#.......
###a.info()
# this gets converted as aky.info(a) thts y self is required
#..........
#