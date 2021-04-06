
def hats(lst):
    cycle = []
    l = lcm(lst[1])
    for i in lst[1]:
        a = i
        cycle.append(i)
        while a < l:
            a += i
            cycle.append(a)
    cycle = sorted(cycle)
    n = lst[0]
    a, n = divmod(n, len(cycle))
    if n > 0:
        sol = cycle[n - 1]
    else:
        sol = 0
    e = ["s", ""][a * cycle[-1] + sol == 1]
    if sol != cycle[n] or sol == 0:
        return "{} minute{}".format((a * cycle[-1]) + sol, e) 
    return None
    
def lcm(x):
    f, r = {}, 1
    for i in x:
        d = get_factors(i)
        for j in set(d):
            f[j] = max(f.get(j, d.count(j)), d.count(j))
    for k in f:
        r *= k ** f[k]
    return r 
    
def get_factors(x):
    p = []
    i = 2
    while x > 1:
        if x % i == 0:
            p.append(i)
            x = x // i
            i = 2
        else:
            i += 1
    return p

