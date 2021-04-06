
def round_number(num, n):
    inc = num; dec = num; res = []
​
    while inc % n != 0:
        inc += 1
    else:
        res.append(inc)
    
    while dec % n != 0:
        dec -= 1
    else:
        res.append(dec)
​
    dif = []
    for i in res:
        dif.append(abs(i-num))
​
    min_dif = min(dif)
​
    end = []
    for i in range(len(dif)):
        if dif[i] == min_dif:
            end.append(res[i])
​
    return max(end)

