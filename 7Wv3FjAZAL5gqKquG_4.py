
def era(er, ip):
  tr = str(round(er/ip*9,2))
  while len(tr) < 4:
    tr += '0'
  if tr[-1] != '0':
    tr = str(round(float(tr) - .01, 2))
  return tr

