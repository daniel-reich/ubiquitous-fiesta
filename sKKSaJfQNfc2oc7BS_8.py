
def sle(m):
    sumY = m[0][1]*m[1][0]+(-1)*m[1][1]*m[0][0]
    if (sumY==0):
        return(False)
    else:
        sumC = m[0][2]*m[1][0]+(-1)*m[1][2]*m[0][0]
        y = int(sumC/sumY)
        x = int((m[0][2]-y*m[0][1])/m[0][0])
        return(x,y)

