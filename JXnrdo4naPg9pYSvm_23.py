
def frac_round(frac, n):
  lst = frac.split('/')
  f1 = int(lst[0]) / int(lst[-1])
  return '{} rounded to {} decimal places is {:.{num}f}'.format(frac, n, f1, num=n)

