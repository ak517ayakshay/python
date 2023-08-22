# anonymus
# def double(e)
#     return 2*e
double=lambda x:x*2
# both of the above are equivivalent
print(double(1))

# main use case is to pass func as argument ex sort a dict

def add(fx,a):
    return 6+fx(a)
cube=lambda x:x**3
print(add(cube,3))