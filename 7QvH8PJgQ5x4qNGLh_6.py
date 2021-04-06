
def countdown(n, txt):
  return '. '.join([str(i) for i in range(1, n + 1)][::-1]) + \
  '.' + ' ' + txt.upper() + '!'

