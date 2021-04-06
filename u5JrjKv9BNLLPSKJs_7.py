
def ways(n, s, lookup):
    if n == 0: return 1
    if n not in lookup:
        lookup[n] = sum(ways(n-v, s, lookup) for v in s if v <= n)
    return lookup[n]
 
num_ways = lambda n, s: ways(n, s, {})

