
def gcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a
​
def sim_prop_frac(max_den):
    fracs = set()
    for den in range(2, max_den + 1):
        for nom in range(1, den):
            g = gcd(den, nom)
            d, n = den // g, nom // g
            fracs.add((n,d))
    return len(fracs)

