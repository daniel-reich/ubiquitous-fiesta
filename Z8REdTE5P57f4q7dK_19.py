
def collatz(n):
    seq = [n]
    k = n
    while True:
        if k % 2 == 0:
            k /= 2
        else:
            k = k*3+1
        seq.append(k)
        if k == 1:
            break
    return len(seq), round(max(seq))

