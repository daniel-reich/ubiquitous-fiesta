
def pop(state):
    l = [ ]
    for a in range(0,len(state)//2 ):
        l.append(a)
    for b in range(len(state)//2, 0 -1 , -1):
        l.append(b)
    return l

