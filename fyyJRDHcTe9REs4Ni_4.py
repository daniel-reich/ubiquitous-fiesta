
def check(d1, d2, k):
  return "One's empty" if any(x==None for x in [d1.get(k),d2.get(k)]) else "Not the same" if d1.get(k) != d2.get(k) else True

