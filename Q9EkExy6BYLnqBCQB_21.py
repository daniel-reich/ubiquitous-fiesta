
def wrap_around(strr, numm):
    global k
    g = len(strr)
    k = strr
    while abs(numm) > g:
        k = k + strr
        g = len(k)
    if numm == 0:
        return(strr)
    if numm > len(strr):
        return(k[int(numm):len(k)]+strr[0:abs(len(k)-int(numm)-len(strr))])
    if numm < len(strr) and numm > 0:
        return(strr[numm:len(strr)]+strr[0:numm])
    if abs(numm) < len(strr) and numm < 0:
        return(strr[len(strr)-abs(numm):len(strr)]+strr[0:len(strr)-abs(numm)])
    if abs(numm) > len(strr) and numm < 0:
        return(strr[len(k)-abs(numm):len(strr)]+strr[0:len(k)-abs(numm)])

