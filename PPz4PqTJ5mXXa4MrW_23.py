
def ulam(n):
    temp=[1,2]
​
    limit=10000
​
    sums=[0 for i in range(2*limit)]
​
    newUlam=2
    sumIndex=1
​
    while(newUlam < limit):
        for i in temp:
            if (i<newUlam):
                sums[i+newUlam] += 1
        while(sums[sumIndex]!=1):
            sumIndex += 1
        newUlam = sumIndex
        sumIndex += 1
        temp.append(newUlam)
  
    return temp[n-1]

