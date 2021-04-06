
D,A=range,len;spotlight_map=lambda g:[[sum(map(lambda k:g[B+k[0]][C+k[1]]if 0<=B+k[0]<A(g)and 0<=C+k[1]<A(g[0])else 0,[(0,0),(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]))for C in D(A(g[B]))]for B in D(A(g))]

