
def initialize(names):
    j=[i.split(" ") for i in names]
    s=[]
    for i in j:
       s.append(i[0][0]+'. '+i[1][0]+'.')
    return s

