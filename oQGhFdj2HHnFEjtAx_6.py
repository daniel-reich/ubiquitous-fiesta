
def slicer(string, slic):
    locs = []
    for c in slic:
        locs.append(string.find(c))
​
    length = len(locs)
    lenStr = len(string)
    start = locs[0]
    endA = locs[length - 1]
    end = endA
    inc = 0
    steps = length - 1
    if(steps >= 1):
        inc = (locs[length - 1] - locs[0]) // steps
​
    if(inc > 0):
        end += 1
    elif(inc < 0):
        end -= 1
​
    res = ''
    
    if(length == 1):
        res = '[' + str(start)
    else:
        res = '['
        if(start == 0 or start == (lenStr - 1)):
            res = res + ':'
        else:
            res = res + str(start) + ':'
            
        if((endA + inc) < 0 or (endA + inc) > lenStr - 1):
            res = res
        else:
            res = res + str(end)
​
        if(inc == 1):
            pass
        else:
            res = res + ':' + str(inc)
    res = res + ']'
    
    return res

