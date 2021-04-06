
def is_unprimeable(num):
    def isPrime(nm):
        # prepare sieve for prime numbers
        ln = [[i, 1] for i in range(nm+1)]
        # Calculate Prime Numbers
        for i in range(2, len(ln)):
            for j in range(2, len(ln)):
                if i * j > nm:
                    break
                ln[i * j][1] = 0
        return True if ln[nm][1] == 1 else False
    if isPrime(num) == 1 and num > 1:
        return "Prime Input"
    # prepare number swapping
    st = str(num)
    lo = []
    for i in range(0,len(st)):
        for j in range(0,10):
            n = int(st[0:i] + str(j) + st[i+1:len(st)])
            if n != 0:
                lo.append(n)
    if all(not isPrime(Z) for Z in lo):
        return "Unprimeable"
    " List of Prime numbers"
    return sorted([Z for Z in lo if isPrime(Z) and Z != num])

