
def gold_distribution(gold):
    mub=[]
    mat=[]
    while True:
        if gold[0]>=gold[-1]:
            mub.append(gold[0])
            gold.pop(0)        
        else:
            mub.append(gold[-1])
            gold.pop(-1)
        if gold[0]>=gold[-1]:
            mat.append(gold[0])
            gold.pop(0)        
        else:
            mat.append(gold[-1])
            gold.pop(-1)
        if gold==[]:
            break
    return [sum(mub),sum(mat)]

