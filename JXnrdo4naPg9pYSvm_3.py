
def frac_round(frac, n):
    return '{} rounded to {} decimal places is {:.{prec}f}'.format(frac,n, eval(frac), prec=n)

