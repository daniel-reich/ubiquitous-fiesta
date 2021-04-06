
def sle(m):
    d=(m[0][0]*m[1][1]-m[1][0]*m[0][1])
    if d==0:
        return False
    y=(m[0][0]*m[1][2]-m[1][0]*m[0][2])/d
    x=(m[1][2]-m[1][1]*y)/m[1][0]
    return int(x),int(y)

