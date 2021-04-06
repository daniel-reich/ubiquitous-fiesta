
def multiply_matrix(m1, m2):
    if len(m1[0]) != len(m2):
        return 'ERROR'
    myans = []
    l = len(m1)
    w = len(m2[0])
​
    for i in range(l):
        temp = []
        for j in range(w):
            temp.append(0)
        myans.append(temp)
​
    for i in range(l):
        for j in range(w):
            for k in range(len(m2)):
                myans[i][j] += m1[i][k]*m2[k][j]
    return myans

