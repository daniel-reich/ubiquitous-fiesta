
def alternate_pos_neg(lst):
    if 0 in lst:return False
    res =[1 if i>0 else 0 for i in lst]
    for i in range(1,len(res)):
        if res[i]==res[i-1]:return False
    return True

