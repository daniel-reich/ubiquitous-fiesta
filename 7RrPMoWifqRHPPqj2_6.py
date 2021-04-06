
def safecracker(start, increments):
    res=[]
    for i in range(len(increments)):
        if i == 0:
            res += [(start+increments[i]*(-1)**(1+i))%100]
        else:
            res += [(res[-1]+increments[i]*(-1)**(1+i))%100]
    return res

