
def three_sum(lst):
    if len(lst)<3:
        return []
    elif len(lst)==3:
        if sum(lst)==0:
            return [lst]
        else:
            return []
    else:
        lst2=[]
        for i in range(len(lst)-2):
            for j in range(i+1,len(lst)-1):
                for k in range(j+1,len(lst)):
                    if lst[i]+lst[j]+lst[k]==0 and [lst[i],lst[j],lst[k]] not in lst2:
                        lst2.append([lst[i],lst[j],lst[k]])
        return lst2

