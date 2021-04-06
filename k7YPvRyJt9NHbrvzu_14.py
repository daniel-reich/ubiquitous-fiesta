
ps=(2,3,6,7,8)
def football(n):
    ret=set()
    for i in range(0,n//ps[0]+1):
        for j in range(0,n//ps[1]+1):
            for k in range(0,n//ps[2]+1):
                for l in range(0,n//ps[3]+1):
                    for m in range(0,n//ps[4]+1):
                        if n==i*ps[0]+j*ps[1]+k*ps[2]+l*ps[3]+m*ps[4]:
                            ret=ret|{(i,j,k,l,m)}
    return len(ret)

