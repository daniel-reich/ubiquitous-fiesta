
def high_low(txt):
  a=list(map(int, txt.split()))
  return "{} {}".format(max(a), min(a))

