class pd:
    def __init__(self):
        self.name=input("enter name ")
        self.occ=input("enter occu ")
    def inf(self):
        print(f"hi {self.name} u r {self.occ}")
v=[]     
u=int(input("enter no of students"))   
for i in range(u):
    r=pd()
    v.append(r)
fd={}
for i in v:
    dicc={f"{i.name}":f"{i.occ}"}
    fd.update(dicc)

print(fd)    
# same thing do for rankcalc