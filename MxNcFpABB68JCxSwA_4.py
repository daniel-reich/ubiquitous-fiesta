
def legendre(n, p):
 return sum([int(p/(n**x)) for x in range(1,20) if (n**x) <= p])

