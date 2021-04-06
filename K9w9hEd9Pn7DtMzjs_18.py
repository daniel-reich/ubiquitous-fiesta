
def high_low(txt):
  lst = txt.split()
  lst = list(map(int, lst))
  mn = str(min(lst))
  mx = str(max(lst))
  st = " ".join([mx,mn])
  return (st)

