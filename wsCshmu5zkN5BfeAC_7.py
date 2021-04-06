
def divisible_by_left(n):
    n = str(n)
    myans = [False]
​
    for i in range(1,len(n)):
        if int(n[i-1]) == 0:
            myans.append(False)
        elif int(n[i]) % int(n[i-1]) == 0:
            myans.append(True)
        else:
            myans.append(False)
    return myans

