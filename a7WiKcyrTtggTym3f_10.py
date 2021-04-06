
def gcd(a, b): return b if a == 0 else gcd(b % a, a)
def lcm(a, b): return (a * b) // gcd(a, b)

