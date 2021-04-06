
def soroban(frame):    
    
    ff, a= [], []    
    for i in range(len(frame)):
        ff.append([])
        for j in frame[i]:
            ff[i].append(j)    
    for i in range(len(ff[1])):
        if ff[1][i] == "O": a.append(5*(10**(6-i)))            
    for i in range(4,len(ff)):
        for j in range(len(ff[i])):
            if ff[i][j] == "|": a.append((i-3)*(10**(6-j)))
    return sum(a)

