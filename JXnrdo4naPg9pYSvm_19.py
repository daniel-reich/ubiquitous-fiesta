
def frac_round(frac, n):
    a, b = [int(_) for _ in frac.split('/')]
    f = str(round(float(a / b), n))
    while len(f.split('.')[1]) < n:
        f += '0'
    return frac + " rounded to " + str(n) + " decimal places is " + f

