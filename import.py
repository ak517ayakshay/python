from math import sqrt,pi
# this imports specific functions from the library
# when we do this there is no need to do math. to call it we can directly use sqrt
w=sqrt(9)
print(w)

from math import *
# this imports all the functions variables etc but not recommended as it leads to confusion if func with same name r present in diff library
from math import sqrt as s
# this imports sqrt as name s
print(s(4))

# to see all the fucn of the particualr library
import math
print(dir(math))

from importexample import intro
intro()