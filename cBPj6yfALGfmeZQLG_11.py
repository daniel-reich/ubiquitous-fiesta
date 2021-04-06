
def vertical_txt(txt):
    t=txt.split()
    m=len(max(t,key=len))
    a=[[' 'for x in range(len(t))] for y in range(m)]
    for x in range(m):
        for y in range(len(t)):
            if x<len(t[y]):
                a[x][y]=t[y][x]
    return a

