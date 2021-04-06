
from math import log
def knight_bfs(a, b, c, d):
    q=[[a,b]]
    count=0
    moves=[[1,2], [1,-2], [2,1], [2,-1], [-1,2], [-1,-2], [-2,1], [-2, -1]]
    while q!=[]:
        for i in moves:
            new=[int(q[0][0])+i[0],int(q[0][1])+i[1]]
            if new==[c,d]:
                return int(log(count)/log(8))+1
            q.append(new)
            count+=1
        q.pop(0)

