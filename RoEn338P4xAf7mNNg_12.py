
def shortest_path(lst):
​
    vert_indeces, point = [],1
    while str(point) in [i for j in lst for i in j]:
        for ind,j in enumerate(lst):
            if str(point) in j: vert_indeces.append(ind)
        point+=1
    
    vert_sum=0
    for ind,i in enumerate(vert_indeces):
        try: vert_sum+=abs(vert_indeces[ind]-vert_indeces[ind+1])
        except IndexError: break
​
    hor_indeces, point = [], 1
    while str(point) in [i for j in lst for i in j]:
        for i in vert_indeces:
            hor_indeces.append(lst[i].index(str(point)))
            point+=1
​
    hor_sum=0
    for ind,i in enumerate(hor_indeces):
        try: hor_sum+=abs(hor_indeces[ind]-hor_indeces[ind+1])
        except IndexError: break
    
    return vert_sum+hor_sum

