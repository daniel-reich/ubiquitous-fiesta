
def sum_of_holes(N):
    oneholes = ['0','4','6','9']
    twoholes = ['8']
    holes = 0
    for i in range(1,N+1):
        i = str(i)
        for j in i:
            if j in oneholes:
                holes+=1
            if j in twoholes:
                holes+=2
    return holes

