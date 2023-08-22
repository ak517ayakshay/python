# you can initialise a multiline string using '''/"""
name = '''akshay
you
are 
legend
'''
print(name)
nam = "akshay"
print(nam[4])
#this prints index of it if index is more than length it throws index out of bound exception
# this can also be done using the for loop
for char in name:
  print(char)
  #char is just like an identifier it can be anything for c in name: ,for a in name:,etc
# ----------------------
# to print till specified position or from specified position we need to use colon :
print(name[2:7])
#this print number from 2 to 6(n-1)always key to remember
print(len(name))
#len is used to calculate the length of string
