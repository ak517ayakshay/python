from datetime import datetime

import os
ct=os.path.getctime("aky.txt")
print(ct)
c=datetime.fromtimestamp(ct).strftime("%y%m%d")
d=int(c)
print(type(c))
print(d,type(d))