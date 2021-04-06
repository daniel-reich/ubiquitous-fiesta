
def pos_neg_sort(lst):
    lst1,lst2,count=[],[],0
    if len(lst)>1:
        for i in lst:
            if i>0:
                lst1.append(i)
        lst1=sorted(lst1)
        for j in lst:
            if j<0:
                lst2.append(j)
            else:
                count=count+1
                lst2.append(lst1[count-1])
    return lst2

