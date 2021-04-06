
def frac_round(frac, n):
  d = round(eval(frac),n)
  s = '{:.'+ str(n) +'f}'
  f = s.format(d) 
  return '{} rounded to {} decimal places is {}'.format(frac, n, f)

