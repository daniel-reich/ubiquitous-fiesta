
def resistance_calculator(resistors):
    l=resistors.copy()
    for i in l:
        if i==0:
            resistors.remove(i)
    if len(resistors)==0:
        return [0,0]
    if len(resistors)<len(l):
        return [0,sum(l)]
    return [round(1/(sum([1/i for i in resistors])),2),round(sum(resistors),2)]

