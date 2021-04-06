
def is_shuffled_well(lst):
    l=[]
    new_l_posi=[]
    new_l_neg=[]
    for i,j in zip(lst,lst[1:]):
        t=i-j
        l.append(t)
​
    if l.count(-1) >= 2 or l.count(1) >= 2:
        for each in range(0,len(l)):
            if l[each]==1:
                new_l_posi.append(each)
            elif l[each]==-1:
                new_l_neg.append(each)
        for posi,num_1 in zip(new_l_posi,new_l_posi[1:]):
            if posi-num_1==-1:
                return False
​
        for neg,num_2 in zip(new_l_neg,new_l_neg[1:]):
            if neg - num_2 == -1:
                return False
​
​
    return True

