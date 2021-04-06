
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
​
​
def sim_prop_frac(max_den):
    res = set()
    for den in range(2, max_den + 1):
        res.add((1, den))
        for num in range(2, den):
            gcd_num_den = gcd(num, den)
            res.add((num // gcd_num_den, den // gcd_num_den))
    return len(res)

