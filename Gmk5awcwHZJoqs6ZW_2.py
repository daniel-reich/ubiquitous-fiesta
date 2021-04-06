
def largest_island(lst):
    if len(lst)==1:return 1
    l=[(x,y) for x in range(len(lst)) for y in range(len(lst[x])) if lst[x][y]==1]
    t=0
    l2=[]
    for i in l:
        if (i[0] + 1, i[1] + 1) in l and (i[0] + 1, i[1] + 1) not in l2:
            l2.append((i[0] + 1, i[1] + 1))
            t+=1
        if (i[0] - 1, i[1] + 1) in l and  (i[0] - 1, i[1] + 1) not in l2:
            l2.append((i[0] - 1, i[1] + 1))
            t+=1
        if (i[0] - 1, i[1] - 1) in l and (i[0] - 1, i[1] - 1) not in l2:
            l2.append((i[0] - 1, i[1] - 1))
            t+=1
        if (i[0] + 1, i[1] - 1) in l and  (i[0] + 1, i[1] - 1) not in l2:
            l2.append((i[0] + 1, i[1] - 1))
            t+=1
        if (i[0] + 1, i[1]) in l and (i[0] + 1, i[1]) not in l2 :
            l2.append((i[0] + 1, i[1]))
            t+=1
        if (i[0] - 1, i[1]) in l and (i[0] - 1, i[1]) not in l2:
            l2.append((i[0] - 1, i[1]))
            t+=1
        if (i[0], i[1] - 1) in l and (i[0], i[1] - 1) not in l2 :
            l2.append((i[0], i[1] - 1) )
            t+=1
        if (i[0], i[1] + 1) in l and (i[0], i[1] + 1) not in l2:
            l2.append((i[0], i[1] + 1))
            t+=1
    if t==0:return 1        
    return t

