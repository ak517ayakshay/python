class employee:
    name=" "
    def __init__(self):
        self.name=input("enter name")
    def show(self):
        print(f"ur name is{self.name}")
class pro(employee):
    # this is the way to inherit
    def __init__(self):
        print("u r pro")
        super().__init__()
        # this is the way to call parent class constructor from child class
    # def show(self):
    #     print("k")
    def show(self):
        print("i am child class method")
        super().show()
        # this class parent class show method
s=pro()
s.show()      
# if super class and child class have method with same name then the child class is given priority   

