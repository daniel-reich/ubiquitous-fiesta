
def sig_figs(num):
  num = num.strip('-')
  if float(num) == 0:
    return 0
  figs = 0
  zeroes = 0
  leading = True
  decimal = False
  for digit in num:
    if digit == '.':
      decimal = True
    elif digit == '0':
      zeroes += 1
    else:
      if leading:
        leading = False
      else:
        figs += zeroes
      zeroes = 0
      figs += 1
  if decimal:
    figs += zeroes
  return figs

