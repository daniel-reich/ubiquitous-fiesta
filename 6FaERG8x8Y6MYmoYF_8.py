
def dice_score(throw):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    total = 0
    #print(total)
    for dice in throw:
        #print(dice)
        if dice == 1:
            a += 1
            #print(a)
        elif dice == 2:
            b += 1
            #print(b)
        elif dice == 3:
            c += 1
            #print(c)
        elif dice == 4:
            d += 1
            #print(d)
        elif dice == 5:
            e += 1
            #print(e)
        else:
            f += 1
            #print(f)
    if a == 3:
        total += 1000
    elif a < 3:
        total += a * 100
    if b == 3:
        total += 200
    if c == 3:
        total += 300
    if d == 3:
        total += 400
    if e == 3:
        total += 500
    elif e < 3:
        total += e * 50
    if f == 3:
        total += 600
    return total

