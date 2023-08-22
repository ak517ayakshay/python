# it helps to change the function and return
def greet(fx):
     # creating a decorator function it should be on top of function whom u decorate
     def mfx():
          print("good morning")
          fx()
          print("thanks for using")
     return mfx
    # Note its return mfx and not mfx() as in mfx fx means function and m means modified
@greet
# this is the way to decorate a function
def hello():
     print("hello")
hello()  
@greet 
def hi():
     print("nkn")
hi()   
greet(hi)
# this also does the same thing

# IMP DECOR FOR ARGUMENTED FUNCTIONS
def introending(fx):
     def mfx(*args,**kwargs):
        #   this is the method to take the arguments in the function *-tuple **-dict
          print("hi")
          fx(*args,**kwargs)
          print("i am done")
     return mfx
@introending     
def add(a,b):
     print(a+b)
add(1,3)     


     