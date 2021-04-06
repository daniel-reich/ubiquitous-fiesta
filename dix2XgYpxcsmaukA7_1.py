
def express_factors(n):
    pfs, lim = [], int(n**0.5) + 2
    for i in range(2, lim):
        cnt = 0
        while n%i == 0:
            n //= i
            cnt += 1
        if cnt: pfs.append(str(i) + ('' if cnt == 1 else '^' + str(cnt)))
    if n > 2: pfs.append(str(n))
    return ' x '.join(pfs)

