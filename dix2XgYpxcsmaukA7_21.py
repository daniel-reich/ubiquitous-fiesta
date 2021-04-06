
def express_factors(n):
    factors = []
    i = 2
    while i < int(n**0.5) + 1:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n != 1:
        factors.append(n)
    ans = []
    for i in sorted(set(factors)):
        temp = factors.count(i)
        if temp > 1:
            ans.append(str(i) + '^' + str(temp))
        else:
            ans.append(str(i))
    return ' x ' .join(ans)

