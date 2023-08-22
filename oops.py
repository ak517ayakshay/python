class aky:
    name="akshay"
    role="legend"
    net=9000
    def info(self):
        print(f"{self.name},{self.role}")
        # self is a object to which this method is called
a=aky()
# this is the way to create object in python
a.name="aky"
# as it is public
print(a.name)    
a.info()
# this gets converted as aky.info(a) thts y self is required
# here self is a like it is called for object a (self oh object jiske liye method call kiya ja ra hai) a is passed as argument to info automaticaaly when self is used
# this replaces this key word and no need of even passing arguments auto is done
b=aky()
b.name="ayus"
b.role="rand"
b.info()

# here self is b like for method b if info does self.name ayus is printed no need of having arguments which we used to have in java,c++
# syntax onjectname = class name
c=aky()
c.info()
# c gets default variables 