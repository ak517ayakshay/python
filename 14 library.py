class library:
    def __init__(self) -> None:
        self._nb=0
        self._n="S"
    @property
    def get(self):
        return self._nb
    @get.setter
    def get(self,n):
        self._nb=self._nb+n
u=[]   
a=library()
for i in range(1,1000):
    o=int(input("1 to add book 2 to exit"))
    if(o==1):
        j=input("enter name of book")
        u.append(j)
        a.get=1

    if(o==2):
        print(u)
        print(a.get)
        break
if(a.get==len(u)):
    print("equal")    