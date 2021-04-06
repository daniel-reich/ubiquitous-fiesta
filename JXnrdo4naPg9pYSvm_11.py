
def frac_round(frac, n):
  txt = '{0:.'+str(n)+'f}'
  return '{} rounded to {} decimal places is {}'.format(frac, n, txt.format(eval(frac)))

