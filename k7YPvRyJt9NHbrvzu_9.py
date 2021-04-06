
def football(score):
    if score == 0:
        return 1
    if score == 1:
        return 0
    ctr = 0
    temp = []
    for a in range(score//8+1):
        for b in range(score//7+1):
            for c in range(score//6+1):
                for d in range(score//3+1):
                    for e in range(score//2+1):
                        if a*8+b*7+c*6+d*3+e*2 == score:
                            ctr += 1
                            temp.append([a,b,c,d,e])
                    
    return ctr

