# function ki return value ko object ki tara use karsakte Getter: A method that allows you to access an attribute in a given class. Setter: A method that allows you to set or mutate the value of an attribute in a class
class ak:
    def __init__(self):
        self._name=int(input("enter value"))
    def show(self):
        print(self._name)
    @property
    # this is the decorator which creates a getter
    def tentimesvaluer(self):
        return 10*self._name    

    @tentimesvaluer.setter
    def ttentimesvalue(self,n):
        self._name=n
        return self._name
    
a=ak()
a.show()
print(a.tentimesvaluer)
ak.tentimesvaluer = 100
print(a.tentimesvaluer)
print(a.tentimesvaluer)
# when u print a.tentimesvalue it automatically prints 10 times the value 
# a.tentimesvalue=100
# u cant directly set it like this u need to use a setter for that 

# did not understand anything in getters setters