
def golomb(n):
    seq = [1,2]
    cnt = 1
    for _ in range(3, n+1):
        if cnt < seq[seq[-1]-1]:
            seq.append(seq[-1])
            cnt += 1
        else:
            seq.append(seq[-1]+1)
            cnt = 1
    return seq

