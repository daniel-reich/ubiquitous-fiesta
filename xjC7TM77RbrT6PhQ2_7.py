
def switches(n):
    seq = ['0', '1']
    for _ in range(n-1):
        seq = ['0' + i for i in seq] + ['1' + i for i in seq[::-1]]
    return seq.index('1' * n)

