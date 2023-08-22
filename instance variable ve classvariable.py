class aky:
    company="apple"
    objcount=0
#    this is the class variable it is shared by all instances of the class
    def __init__(self):
        self.name=input("enter name")
        aky.objcount+=1
# name is the instance variable which is given to each object seprately
    def show(self):
        print(self.name ,self.company,aky.objcount)    
        
a=aky()
a.show()
b=aky()
b.company="hp"
# when u do this company is created which acts as the instance variable to class b note here original company is not changed that is class variable it cannot be manipulated by object if instance variable is there that is printed when it is not there class variable is found
aky.company="google"
# this is the way to modifiy an class variable
a.show()
b.show()
c=aky()
c.show()