
def replace_next_largest(lst):
    lst2 = []
    slst = sorted(lst)
    slst.append(-1)
  
    for i in lst:
        for j in range(len(slst)-1):
            if slst[j] == i:
                lst2.append(slst[j+1])
    return lst2

