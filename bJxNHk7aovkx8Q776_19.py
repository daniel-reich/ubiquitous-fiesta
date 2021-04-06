
def gold_distribution(gold):
    Mubashir=[]
    Matt=[]
    while len(gold)!=0:
        Mubashir.append(max(gold[0], gold[-1]))
        gold.remove(max(gold[0], gold[-1]))
        Matt.append(max(gold[0], gold[-1]))
        gold.remove(max(gold[0], gold[-1]))
    return [sum(Mubashir), sum(Matt)]

