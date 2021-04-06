
def gold_distribution(gold):
    [mub,matt] = [0,0]
    while len(gold)!=0:
        m = max(gold[0],gold[-1])
        mub+=m
        gold.pop(gold.index(m))
        if len(gold)==0:break
        m = max(gold[0],gold[-1])
        gold.pop(gold.index(m))
        matt+=m
    return [mub,matt]

