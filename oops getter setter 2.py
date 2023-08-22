class aky:
    def __init__(self) -> None:
        self.__id=0
    @property
    def incre(self):
        return self.__id
    @incre.setter
    def incre(self,n):
        self.__id=n
        return self.__id
a=aky()
for i in range(4):
    a.incre=i
    print(a.incre)    