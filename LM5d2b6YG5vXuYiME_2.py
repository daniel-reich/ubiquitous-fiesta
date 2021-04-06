
def can_enter_cave(x):
    q=[]
    for i in range(len(x)):
        if x[i][0]==0:
            q.append((i,0))
    while q!=[]:
        p=q.pop(-1)
        if p[1]==len(x[0])-1:
            return True
        else:
            a=p[0];b=p[1]+1
            if x[a][b]==0:    
                if (a,b) not in q:
                    q.append((a,b))
                    for i in range(1,len(x),1):
                        if a+i<len(x):
                            if x[a+i][b]==0 and ((a+i,b)) not in q:
                                q.append((a+i,b))
                        if a-i>=0:
                            if x[a-i][b]==0 and ((a-i,b)) not in q:
                                q.append((a-i,b))
    return False

