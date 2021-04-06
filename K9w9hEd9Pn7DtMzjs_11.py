
def high_low(txt):
  i = list(map(int, txt.split( )))
  return ' '.join([str(max(i)), str(min(i))])

