
def odd_square_patch(lst):
    m = len(lst)
    n = len(lst[0])
    r = min(m,n)
    for s in range(r,0,-1):
        for i in range(m-s+1):
            for j in range(n-s+1):
                count = 0
                for k1 in range(s):
                    for k2 in range(s):
                        if lst[i+k1][j+k2]%2 == 1:
                            count +=1
                if count == s*s:
                    return s
    return 0

