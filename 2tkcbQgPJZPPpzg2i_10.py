
def sum_of_holes(N):
    hd={'0':1,'4':1,'6':1,'8':2,'9':1}
    s=0
    for v in range(1,N+1):
        for d in str(v):
            if d in hd:
                s=s+hd[d]           
    return s

