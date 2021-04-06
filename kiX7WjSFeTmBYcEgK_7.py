
def major_sum(lst):
    new = []
    zero = lst.count(0)
    pos = sum(i for i in lst if i>0)
    neg = (sum(j for j in lst if j<0))
    new.append(zero)
    new.append(pos)
    new.append(neg)
    
    return neg if abs(neg) > zero and abs(neg) > pos else max(new)

