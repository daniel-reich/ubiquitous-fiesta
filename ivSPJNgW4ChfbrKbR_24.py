
def soroban(frame):
    value = 0
    frame = [i[::-1] for i in frame]
    fives = frame[:2]; ones = frame[3:]; ones_multi = {i:0 for i in range(7)}
​
    for f in range(7):
        if fives[0][f] == "|":
            value += 5 * 10**(f)
​
    for i in range(5):
        for o in range(7):
            if ones[i][o] == "|":
                ones_multi[o] = i
​
    for k,v in ones_multi.items():
        value += v * 10**k
​
    return value

