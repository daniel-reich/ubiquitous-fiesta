
def bomb(lst):
    def f(x1,y1,x2,y2):return int(((x2-x1)**2+(y2-y1)**2)**0.5)
    a, b, c = lst
    for i in range(51):
        for j in range(51):
            if f(i,j,a[0],a[1])==int(a[2]*0.3435) and \
            f(i,j,b[0],b[1])==int(b[2]*0.3435) and \
            f(i,j,c[0],c[1])==int(c[2]*0.3435): return (i,j)

