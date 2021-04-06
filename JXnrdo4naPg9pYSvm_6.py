
def frac_round(frac, n):
  rounded = str(round(eval(frac),n))
  dot = rounded.find('.')
  places = len(rounded[dot+1:])
  return frac + ' rounded to ' + str(n) + ' decimal places is ' + rounded + ('0' * (n-places))

