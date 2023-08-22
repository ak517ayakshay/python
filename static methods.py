# static method is just like a normal method which u wpould define outside the class it has no self with it.it can be called by both object and class name
class aky:
   def __init__(self) -> None:
      self.n=int(input("ent"))
   @staticmethod
   def add(a,b):
      return a+b
a=aky()
b=aky()
print(a.add(a.n,6))
# object calling
print(aky.add(a.n,b.n))
# this is called by class  name
# u may argive if u want to do this just place this method outside it still works ya u r right but this is used like if u r gicing this class to any one and u want ur class users to have benefit out of it
             