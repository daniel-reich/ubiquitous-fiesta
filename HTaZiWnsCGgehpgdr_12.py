
import math
​
def license_plate(s, n):
    wrd = ''
    plchldr=''
    lst=s.split('-')
    for i in range(0, len(lst)):
        wrd += lst[i]
    if len(wrd)%n==0:
        for i in range(0, math.floor(len(wrd)/n+1)):
            if i==math.floor((len(wrd)/n)):
                plchldr=plchldr+wrd[n*i:n+(n*i)]
            else:
                plchldr=plchldr+wrd[n*i:n+(n*i)]+'-'
        return plchldr.upper()[0: int(len(plchldr))-1]
    else:
        for i in range(0, len(wrd)%n):
            plchldr=plchldr+wrd[i]
        plchldr=plchldr+'-'
        wrd = wrd[len(wrd)%n:]
        for i in range(0, math.floor(len(wrd)/n+1)):
            if i==math.floor((len(wrd)/n)):
                plchldr=plchldr+wrd[n*i:n+(n*i)]
            else:
                plchldr=plchldr+wrd[n*i:n+(n*i)]+'-'
        return plchldr.upper()[0: int(len(plchldr))-1]

