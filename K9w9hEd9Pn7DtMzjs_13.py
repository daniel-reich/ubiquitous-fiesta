
def high_low(txt):
  lst = [int(i) for i in txt.split()]
  return "{} {}".format(max(lst), min(lst))

