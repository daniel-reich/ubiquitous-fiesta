
def initialize(names):
    s=[]
    for i in range(len(names)):
        a,b=names[i].split()
        s.append(a[0]+'. '+b[0]+'.')
    return s

