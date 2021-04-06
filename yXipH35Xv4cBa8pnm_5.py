
def microwave_buttons(time):
    t = list(map(int,time.split(':')))
​
​
    s = t[1]+60*t[0]
​
    a = s // 30
    r = s % 30
    if a == 0 and r == 0:
        return 1
​
    if r == 0:
        b = a + 1
    else:
        b = a + len(str(r)) + 1
​
    t2 = time.replace(':','')
​
    b1 = 1
    for i in range(4):
        if int(t2[i]) > 0:
            b1 += 4-i
            break
​
    if b1 < b:
        return b1
    return b

