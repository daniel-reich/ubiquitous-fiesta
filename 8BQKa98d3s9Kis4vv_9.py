
def final(r, c, i):
    matrix=[]
    for a in range(r):
        matrix.append([])
        for b in range(c):
            matrix[-1].append(0)
    for item in i:
        num=int(item[0])
        if item[1]=='r':
            matrix[num]=list(map(lambda x : x+1 , matrix[num]))
            
        if item[1]=='c':
            for m in matrix:
                m[num]+=1
    return matrix

