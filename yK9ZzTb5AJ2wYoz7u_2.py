
def floyd(up_to = None, n_row = None):
    myans = []
    if up_to != None:
        a = 1
        b = 1
        while a <= up_to:
            temp = []
            for i in range(b):
                temp.append(a)
                a += 1
            myans.append(temp)
            b += 1
    else:
        a = 1
        b = 1
        for j in range(n_row):
            temp = []
            for i in range(b):
                temp.append(a)
                a += 1
            myans.append(temp)
            b += 1
​
    return myans

