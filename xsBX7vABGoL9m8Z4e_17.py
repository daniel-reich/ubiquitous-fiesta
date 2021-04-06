
import re
def changeTime(tmStr, hrD, mnD, scD, msD):
    msStr = tmStr.split(',')
    ms = int(msStr[1])
    hmsS = msStr[0].split(':')
    hr = int(hmsS[0])
    mn = int(hmsS[1])
    sc = int(hmsS[2])
​
    ms += msD
    if(ms > 999):
        ms -= 1000
        sc += 1
​
    sc += scD
    if(sc > 59):
        sc -= 60
        mn += 1
​
    mn += mnD
    if(mn > 59):
        mn -= 60
        hr += 1
​
    hr += hrD
    if(hr > 11):
        hr -= 12
​
    tmStr = '{:02d}:{:02d}:{:02d},{:03d}'.format(hr, mn, sc, ms)
    #print(tmStr)
    return tmStr
    
def sync_subs(subT, tInc):
    errStr = 'There is a problem with the second argument'
​
    #-----------------------------
    # Time Increment
    msS = tInc.split(',')
    if(len(msS) != 2):
        print(errStr)
        return errStr
    if(len(msS[1]) != 3):
        print(errStr)
        return errStr
    msD = int(msS[1])
​
        
    hmsS = msS[0].split(':')
    if(len(hmsS) != 3):
        print(errStr)
        return errStr
    if(len(hmsS[0]) != 2 or len(hmsS[1]) != 2 or len(hmsS[2]) != 2):
        print(errStr)
        return errStr
    hrD = int(hmsS[0])
    mnD = int(hmsS[1])
    scD = int(hmsS[2])
    if(hrD > 11 or mnD > 59 or scD > 59):
        print(errStr)
        return errStr
​
    #print('Time : {:02d} {:02d} {:02d} {:03d}'.format(hrD, mnD, scD, msD))
    
    pattern = '[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}'
    lst = re.findall(pattern, subT)
    #print(lst)
​
    ln = len(lst[0])
    for mtchStr in lst:
        newStr = changeTime(mtchStr, hrD, mnD, scD, msD)
        #print('Match : {} {}'.format(mtchStr, subT))
        ind = subT.index(mtchStr)
        #print('INDEX : {} {} {}\n\n'.format(ind, mtchStr, subT))
        subT = subT[0: ind] + newStr + subT[ind + ln:]
        #print('Match : {} {}'.format(mtchStr, newStr))
​
    #print(subT)
    return subT

