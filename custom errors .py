# this is the way to raise the errors by urself
b=int(input("enter the value between 5 and 8"))
if(b>8 or b<5):
    raise ValueError("the value entered must be between 5 and 8")
# like this u can raise the error by urself