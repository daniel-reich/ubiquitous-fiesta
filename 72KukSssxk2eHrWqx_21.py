
def char_at_pos(r, s):
    nl=[]
    for i in range(-1,-len(r)-1,-1):
        
            
        if (s=="odd") & (i %2 !=0):
            nl.append(r[i])
        elif (s=="even") & (i %2 ==0):
            nl.append(r[i])
    if type(r)==str:
        return ''.join(nl[::-1])
    else:
        return nl[::-1]

