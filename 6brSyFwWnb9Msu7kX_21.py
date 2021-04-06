
def pos_neg_sort(lst):
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]<0 or lst[j]<0:
                continue
            elif lst[j]<lst[i]:
                lst[j],lst[i] = lst[i],lst[j]
    return lst

