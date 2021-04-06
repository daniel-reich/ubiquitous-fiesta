
def lcm(n1, n2):
    max_n = max(n1, n2)
    min_n = min(n1, n2)
    r = n1* n2
    return min([max_n * i for i in range(1,min_n+1) if max_n*i %min_n==0])

