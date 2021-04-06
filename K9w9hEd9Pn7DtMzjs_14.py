
def high_low(txt):
  return ' '.join([str(max(int(x) for x in txt.split())),min(txt.split())])

