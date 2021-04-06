
def tower_of_hanoi(disks, move):
    p=0
    m=(((0,1),(0,2),(1,2)),((0,2),(0,1),(1,2)))
    t=[[i for i in range(1,disks+2,1)],[disks+1],[disks+1]]
    a=disks%2
    while move>0:
        d1=t[m[a][p][0]][0]
        d2=t[m[a][p][1]][0]
        if d1<d2:
            t[m[a][p][1]].insert(0,d1)
            t[m[a][p][0]].pop(0)
        else:
            t[m[a][p][0]].insert(0,d2)
            t[m[a][p][1]].pop(0)
        move-=1
        p+=1
        p=p%3
    for i in range(len(t)):
        t[i].reverse()
        t[i].pop(0)
    return tuple(t)

