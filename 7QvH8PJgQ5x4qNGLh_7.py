
def countdown(n, txt):
  numbers = '. '.join(str(i) for i in range(n,0,-1))
  return numbers + '. {}!'.format(txt.upper())

