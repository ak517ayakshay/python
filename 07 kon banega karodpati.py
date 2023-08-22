def ca(c,*n):
    # here u should first take the argument c and then *n as *n accepts only keyword only argument 
    b = [4, 3, 3, 1, 3]
    # print(n[c],b[c])
    if n[c] == b[c]:
        
        print("sai javab")
    else:
        print("sai javab hai", b[c])

print("chaliye shuru karte hai khon banega karodpati")
print("who among the following is the best cricketer")
print("1) yuvraj singh        2) dhoni")
print("3) virat kholi         4) ayush pratap singh")

b = []
c = 0

o = int(input("Press your choice: "))
b.append(o)
ca(c,*b)
c = c + 1
print("aarnav choudhary is a?")
print("1) ytber      2) legend")
print("3) allrounder 4) content creator")

o = int(input("Press your choice: "))
b.append(o)

ca(c,*b)
c = c + 1
print("Who is the tallest among all?")
print("1) akshay       2) jatis")
print("3) aarnav       4) avinash")

o = int(input("Press your choice: "))
b.append(o)

ca(c,*b)
c = c + 1
print("Who studies a lot?")
print("1) aadith      2) aarnav")
print("3) goutham     4) chirag")

o = int(input("Press your choice: "))
b.append(o)

ca(c,*b)
c = c + 1
print("Who is the smartest among all?")
print("1) akshay       2) jatis")
print("3) aarnav       4) avinash")

o = int(input("Press your choice: "))
b.append(o)
ca(c,*b)
g= [4, 3, 3, 1, 3]
if(g==b):
    print("Ek karod")
