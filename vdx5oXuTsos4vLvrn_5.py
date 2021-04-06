
def kaprekarNumbers(p, q):
    res = []
    for n in range(p, q + 1):
        len_n = len(str(n))
        str_n2 = str(n * n)
        if ((len_n == 1 and n == 1) or
                (len(str_n2) > 1 and int(str_n2[:-len_n])
                 + int(str_n2[-len_n:]) == n)):
            res.append(n)
    return ' '.join(str(n) for n in res) if res else 'INVALID RANGE'

