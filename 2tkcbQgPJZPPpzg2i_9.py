
def sum_of_holes(N):
    dix = {0:1, 4:1, 6:1, 8:2, 9:1}
    sum= 0
    for i in range (1, N+1):
        if i <=9 and i in dix:
            sum+=dix[i]
        else:
            j= str(i)
            for k in j:
                if int(k) in dix:
                    sum+=dix[int(k)]
            
    return sum

