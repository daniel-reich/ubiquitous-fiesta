
def frac_round(frac, n):
    numerator, denominator = frac.split('/')
    result = round(int(numerator)/int(denominator), n)
    return '{frac} rounded to {n} decimal places is {result:0.{n}f}'.format(frac=frac, n=n, result=result)

