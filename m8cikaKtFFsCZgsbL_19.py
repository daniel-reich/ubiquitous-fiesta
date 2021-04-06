
def waterjug(start, goal):
    if start[2]==goal[2]:
        return 0
    if start[2]!=sum(goal):
        return 'No solution.'
    pour=((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0))
    q=[[[0,0,start[2]]]];k=0
    while k<10:
        t=[]
        for i in range(len(q[k])):
            for p in pour:
                temp=[0,0,0]
                if q[k][i][p[0]]!=0 and q[k][i][p[1]]!=start[p[1]]:
                    dif=start[p[1]]-q[k][i][p[1]]
                    if dif>=q[k][i][p[0]]:                 
                        temp[p[1]]=q[k][i][p[1]]+q[k][i][p[0]]
                        temp[p[0]]=0
                        temp[p[2]]=q[k][i][p[2]]
                    else:
                        temp[p[1]]=start[p[1]]
                        temp[p[0]]=q[k][i][p[0]]-dif
                        temp[p[2]]=q[k][i][p[2]]
                if temp!=[0,0,0]:
                    t.append(temp)
                    if temp==goal:
                        return k+1
        q.append(t)
        k+=1
    return 'No solution.'

