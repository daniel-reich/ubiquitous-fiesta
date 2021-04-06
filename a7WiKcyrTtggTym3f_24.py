
gcd = lambda a,b: gcd(b,a%b) if b else a
lcm = lambda a,b: a*b/gcd(a,b)

