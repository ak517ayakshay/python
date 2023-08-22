def aky(a,b):
  pass
#this is the way to declare a function when u write pass u will let compiler know tht u will wrote the function later
def aa(a,b):
  return a,b
# this returns a tuple
# return [a,b]
# this returns a list



def fact(i):
  if (i == 0):
    return 1
  else:
    return i * fact(i - 1)


n = int(input("enter no "))
print(fact(n))
#function arguments
print("\n")
def average(a,b):#---first case
  print((a+b)/2)
  #this require value of a and b
def average(a=9,b=10):#these r default variabless
  print((a+b)/2)
  
average(10,2)#this is for 1st case
    
def see(a,b=9):
  #here a is required argument and b is default
  print(a+b)

see(8)


def hh(n=9,m=7):
  print(n*m)
hh(m=6)
  #ny this u can directly give the value of m without giving value of n 


def wtf(*n):
    # this accepts the arguments as tuples u can compare it to base address in c
    s=0
    for i in n:
        s=s+i
    print(s)
    print(len(n))
    #by this u can see the length of the tuple 

wtf(3,4,5)
