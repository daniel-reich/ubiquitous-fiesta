
def frac_round(frac, n):
  a, b = (int(e) for e in frac.split('/'))
  res = str(round(a / b, n)).split('.')[1]
  if len(res) < n:
    res = res + '0'*(n-len(res)) 
  return '{0} rounded to {1} decimal places is {2}'.format(frac, n, str(a//b) + '.' + res)

