
def fibo_word(n):
    if n < 3:
        return 'invalid'
    seq = ['b', 'a']
    for _ in range(3, n + 1):
        seq.append(seq[-1] + seq[-2])
    return ', '.join(seq)

