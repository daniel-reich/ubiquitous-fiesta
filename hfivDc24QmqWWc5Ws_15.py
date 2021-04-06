
def eratosthenes(n):
    res = [0,0] + [1]*(n-2)
    for i in range(2, int(n**0.5)+1):
        res[i*i::i] = [0] * ((n-1)//i - i + 1)
    return [i for i,v in enumerate(res) if v]

