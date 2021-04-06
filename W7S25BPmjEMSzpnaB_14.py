
def bonacci(N, k):
    b = [0]*(N-1)+[1]
    while True:
        if len(b)>=k:
            break
        j= 0
        for i in range(N):
            j+=b[len(b)-i-1]
        b.append(j)
    return b[k-1]

