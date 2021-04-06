
def get_lucky_number(size, nth):
    list1=[x for x in range(1,size+1,2)]
    list2=list1.copy()
    y=1
    idx=list2[y]
    for x in list2:
        if len(list2)<=idx:
            return (list2[nth-1])
        else:
            idx=list2[y]
            list2=[x for x in list2 if ((list2.index(x)+1)%int(idx)!=0)]
            y+=1

