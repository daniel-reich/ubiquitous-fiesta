
def countdown(n, txt):
  return '. '.join([str(i) for i in range(n, 0, -1)])  + '. ' + txt.upper() + '!'

