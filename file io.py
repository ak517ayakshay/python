# opening a file
f=open("myfile.txt",'r')
# f=open("myfile.txt")
# this also works as r mode is default
text=f.read()
# reading a file and storing it in text
print(text)
# to write a file
f=open("myfile1.txt",'w')
f.write("akshay come on man u can")
# this 1st clears the file and then writes if file is not present it creates
f=open("myfile1.txt","a")
f.write("  \ni am file of fileio.py")
# to create a file throws error if already exits
# f=open("myfile2.txt",'x')
# to open any img,jpj,.exe,img
f=open("que.png",'rb')
f.close()
with open("myfile1.txt",'a') as f:
    f.write("\n i am inside with")