
def stem_plot(lst):
    myDict = {}
    temp = []
    myans = []
    for i in range(len(lst)):
        x = str(lst[i])[:-1]
        if x == '':
            x = 0
        else:
            x = int(x)
        if x not in myDict:
            myDict[x] = [str(lst[i])[-1]]
        else:
            myDict[x].append(str(lst[i])[-1])
​
    for k,v in myDict.items():
        v = sorted(v)
        temp.append([k,v])
    temp = sorted(temp)
​
    for i in range(len(temp)):
        myans.append(str(temp[i][0])+' | '+' '.join(temp[i][1]))
​
    return myans

