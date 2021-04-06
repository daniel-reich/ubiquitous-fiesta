
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
​
def mixed_number(frac):
    pos = frac.find("/")
    n, D = int(frac[:pos]), int(frac[pos+1:])
    signal = "-" if n < 0 else ""
    d, r = abs(n)//D, abs(n) % D; v = gcd(r, D)
    if not d and not r: return "0"
    return signal +(str(d) if d else "")+((" " if d else "")+str(r//v)+"/"+str(D//v) if r else "")

