f=open("myfile1.txt","r")
while True:
    line=f.readline()
    print(line)
    if not line:
        print("reached eof")
        break
f=open("myfile.txt","w")
line=["aksha\n","kkk\n"]    
f.writelines(line)
# this seems useless as \n \n is used