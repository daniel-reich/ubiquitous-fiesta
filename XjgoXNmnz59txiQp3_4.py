
def split(number):
    if number == 1:
        return 1
    myans = []
    for g in range(1,number):
        v = number // g
        if number % g == 0:
            myans.append(v**g)
        else:
            t = (v**(g-1))*(number-v*(g-1))
            myans.append(t)
​
            v += 1
            t = (v**(g-1))*(number-v*(g-1))
            myans.append(t)
​
    return max(myans)

