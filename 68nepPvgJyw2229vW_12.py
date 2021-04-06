
def pairwise_swap(list_of_elements):
    if len(list_of_elements)%2 == 0:
        lst = list_of_elements.copy()
        flag = 0
    else:
        lst = list_of_elements[:-1].copy()
        flag = 1
​
    for i in range(0,len(lst)-1,2):
        lst[i],lst[i+1] = lst[i+1],lst[i]
 
    if flag == 0:
        return lst
    else:
        lst.append(list_of_elements[-1])
        lst_str = [str(a1) for a1 in lst ]
        a2 = []
        for i in lst_str:
            a2_str = [ord(c) for c in i]
            a2.append(sum(a2_str))
​
        a2_max_inx = [i for i, j in enumerate(a2) if j == max(a2)]
​
        if len(a2_max_inx) > 1:
            lst[-1],lst[0] = lst[0],lst[-1]
            return lst
        else:
            lst[-1], lst[a2_max_inx[0]] = lst[a2_max_inx[0]], lst[-1]
            return lst

