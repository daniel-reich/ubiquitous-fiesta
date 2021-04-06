
def shuffle_count(num):
    lst = [i for i in range(1,num+1)]
    out = 0
    lst_shuff = []
    temp = lst
    while lst_shuff != lst:
        lst_shuff = []
        for i,j in zip(temp[:int(len(temp)/2)],temp[int(len(temp)/2):]):
            lst_shuff.append(i)
            lst_shuff.append(j)
        out+=1
        temp = lst_shuff
​
    return out

