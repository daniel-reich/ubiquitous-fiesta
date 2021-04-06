
def consecutive_sum(n):
    for i in range(0,n-1):
        ctr = i
        for j in range(i+1,n):
            ctr += j
            if ctr == n:
                return True
            elif ctr > n:
                break
    return False

