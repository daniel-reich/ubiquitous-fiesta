
def dice_score(throw):
    mydict = {}
    for i in throw:
        if i not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1
​
    myscore = 0
​
    if 1 in throw:
        if mydict[1] >= 3:
            myscore += 1000
            mydict[1] -= 3
    if 6 in throw:
        if mydict[6] >= 3:
            myscore += 600
            mydict[6] -= 3
    if 5 in throw:
        if mydict[5] >= 3:
            myscore += 500
            mydict[5] -= 3
    if 4 in throw:
        if mydict[4] >= 3:
            myscore += 400
            mydict[4] -= 3
    if 3 in throw:
        if mydict[3] >= 3:
            myscore += 300
            mydict[3] -= 3
    if 2 in throw:
        if mydict[2] >= 3:
            myscore += 200
            mydict[2] -= 3
    if 1 in throw:
        if mydict[1] >= 0:
            myscore += mydict[1]*100
            mydict[1] = 0
    if 5 in throw:
        if mydict[5] >= 0:
            myscore += mydict[5]*50
            mydict[5] = 0
    return myscore

