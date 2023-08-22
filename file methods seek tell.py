f=open("myfile1.txt","r")
f.seek(10)
# this means that dont read the file from starting skip 10 letters and then do read allows to move pointer to specific point
d=f.read(5)
# this means read only 5 bytes of the data
print(f.tell())
# this tells the current posi of the file
print(d)
f=open("myfile2.txt","w")
f.write("hello world")
f.truncate(4)
# this sets the max size of file to 4 bytes ie only 4 charcters
f=open("myfile2.txt","r")
h=f.read()
print(h)