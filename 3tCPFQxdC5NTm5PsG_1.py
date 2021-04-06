
from itertools import*
d=lambda x,y:((x[0]-y[0])**2+(x[1]-y[1])**2)**.5
f=lambda a,b,c,d,e,k:a*(d-k)+c*(k-b)+e*(b-d)==0
find_triangles=lambda l:sum(not f(a[0],a[1],b[0],b[1],c[0],c[1])and(d(a,b)==d(a,c)or d(a,b)==d(c,b)or d(a,c)==d(c,b))for a,b,c in combinations(l,3))

