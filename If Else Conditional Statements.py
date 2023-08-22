a = int(input("Enter ur age"))
if(a>=18):
  #colon put here is just like curly braces which are in c and space left before the string is called as the indentation space
  print("you can vote")
  print("u can drive")
else:
  print("you cannot vote")
  print("you cannot drive")
  a = int(input("Enter ur age"))
if (a >= 18):
  #colon put here is just like curly braces which are in c and space left before the string is called as the indentation space
  print("you can vote")
  print("u can drive")
else:
  print("you cannot vote")
  print("you cannot drive")
#now lets see elif its like else if
b = int(input("enter the number"))
if (b < 0):
  print("number is negative")
elif (b == 0):
  print("its zero")
else:
  print("+ve")
#now lets see nested if
c = int(input("enyter"))
if (c > 0):
  print("no is +ve")
  if (c % 2 == 0):
    print("even")
    if (c / 2 == 1):
      print("no is 2")
  else:
    print("odd")
else:
  print("-ve")
# to add multiple conditions in if statement use and and or in words
#eg if(a>0 and a<100)
#now lets see elif its like else if
b=int(input("enter the number"))
if(b<0):
  print("number is negative")
elif(b==0):
  print("its zero")
else:
  print("+ve")
#now lets see nested if
c=int(input("enyter"))
if(c>0):
  print("no is +ve")
  if(c%2==0):
    print("even")
    if(c/2==1):
      print("no is 2")
  else:
    print("odd")
else:
  print("-ve")
