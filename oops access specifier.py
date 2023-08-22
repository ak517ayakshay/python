# in python there is no strict concept of it but we can access them indirectly
class employee:
    
    def __init__(self) -> None:
        self._v=1
        # this is the way to declare protected variable
        self.__name=input("enter name")
        # this is the way to declare a private variable(__ double underscore)
a=employee()
# print(a.__name)
# u cannot access it as it is private
# to access a private variable _classname__attricbutname
print(a._employee__name)
# indirect accessing called as NAME MANGLING
# name mangling is done so that there must not be accidental reuse and modification happens there 
# ie u declare a = 9;
# but later u change a=1
# value of a gets changed but if u use __a it is renamed as _classname__a=9 this is the way to mangle
print(a._v)
# u can access 