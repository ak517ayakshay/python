with open("myfile.txt",'r') as f:
    i=0
    while(True):
        t=f.read(1)
        f.seek(12+i)
        if t.startswith('+'):
            q=f.read(12)
            if(q.isnumeric()):
                print(t+q)
        if not t:
            break
        i=i+1