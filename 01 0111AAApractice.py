import os
g=(os.listdir("pics"))
c=0
for i in g:
    c=c+1

    if(i.endswith(".png") or i.endswith(".jpg")):
     op=os.path.join("pics",i)
    #  os.rename takes the path to change  the name of source and destination thts y its necessary to generate the path
     nn=f"{c}.png"
     np=os.path.join("pics",nn)
     os.rename(op,np)
print(os.listdir("pics"))