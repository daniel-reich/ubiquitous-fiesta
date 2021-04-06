
def jumping_frog(n, stones):
    v = [0]
    loc = 0
    ctr = 1
​
    while loc < n:
        if stones[loc] == 0:
            ctr = 999
            break
        elif loc + stones[loc] not in v:
            loc += stones[loc]
            v.append(loc)
            ctr += 1
        elif v.count(loc + stones[loc]) < 2:
            loc += stones[loc]
            v.append(loc)
            ctr += 1
        elif loc - stones[loc] >= 0:
            if loc - stones[loc] not in v:
                loc -= stones[loc]
                v.append(loc)
                ctr += 1
            elif v.count(loc - stones[loc]) < 2:
                loc -= stones[loc]
                v.append(loc)
                ctr += 1
        else:
            ctr = 999
            break
​
    v = [0]
    loc = 0
    ctr2 = 1
​
    while loc < n:
        if stones[loc] == 0:
            ctr2 = 999
            break
        elif loc - stones[loc] >= 0:
            if loc - stones[loc] not in v:
                loc -= stones[loc]
                v.append(loc)
                ctr2 += 1
            elif v.count(loc - stones[loc]) < 2:
                loc -= stones[loc]
                v.append(loc)
                ctr2 += 1
        if loc + stones[loc] not in v:
            loc += stones[loc]
            v.append(loc)
            ctr2 += 1
        elif v.count(loc + stones[loc]) < 2:
            loc += stones[loc]
            v.append(loc)
            ctr2 += 1
        else:
            ctr2 = 999
            break
​
    if ctr < ctr2:
        return ctr
    elif ctr2 < ctr:
        return ctr2
    elif ctr == 999:
        return 'no chance :-('
    else:
        return ctr

