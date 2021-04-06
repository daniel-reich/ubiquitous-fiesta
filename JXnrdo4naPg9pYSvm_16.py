
def frac_round(frac, n):
  ans = round(eval(frac), n)
  ans = format(ans, '.'+str(n)+'f')
  return '{frac} rounded to {n} decimal places is {ans}'.format(frac=frac, n=n, ans=ans)

