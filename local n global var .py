x=1
# global variable
print(x)
def helo():
    x=9
    global d
    # u cant  initalize  directly
    print(f"i am local {x}")
    d=8
helo()
print("glo",x)    
print(d)
