class emp:
    def __init__(self) -> None:
         self.name=input("enter name")
         self.id=int(input("enter id"))
    def show(self):
         print(self.name,self.id)
class pro(emp):
     def __init__(self) -> None:
          super().__init__()
          self.iq=input("enter ur iq")
     def show2(self):
         super().show()  
         print(f"u have an iq of {self.iq}")
class stu(emp):
     def __init__(self) -> None:
          super().__init__()
          self.mark=int(input("enter ur marks babygirl"))
     def showq(self):
         super().show()
         print(self.mark)
i=int(input("1 for pro 2 for stu "))
if(i==1):
     a=pro()
     a.show2()
else:
     b=stu()
     b.showq()   

                                    