
def frac_round(frac, n):
  return '{} rounded to {} decimal places is {:0<{}}'.format(frac, n, round(eval(frac), n), n+len(str(eval(frac)).split('.')[0])+1)

