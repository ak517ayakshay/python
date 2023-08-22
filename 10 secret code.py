def three():

    g="abcdefghijklmnopqrstuvwxyz"
    b=[ ]
    for i in range(3):
     h=random.choice(g)
     b.append(h)
    return b  
    
def ls(*b):
    s=" "
    for i in b:
        s=s+i    
    return s    

import random
if(2>0):
    s=int(input("1 to code 2 to decode - "))
    match s:
       case 1:
           q=input("enter the string u want to code - ")
           w=len(q)
           if(w<3):
               
            print(q[::-1])
           else:
                k=q[0]
                l=list(q)
                l.pop(0)
                l.append(k)
                g=ls(*l)
                o=three()
                o=ls(*o)
                n=three()
                n=ls(*n)
                n=n.replace(' ','')
                g=g.replace(' ','')
                o=o.replace(' ','')
                print(o+g+n)
       case 2:
         q=input("enter the string u want to decode - ")
         w=len(q)
         if(w<3):
          print(q[::-1])
         else:
            w=q[3:-3] 
            r=w[len(w)-1]
            w=w[:-1]
            w=r+w   
            print(w)     
                      