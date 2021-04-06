
def check(d1, d2, k):
  return "One's empty" if (k in d1 and k not in d2) or (k in d2 and k not in d1) else "Not the same" if d1[k]!=d2[k] else True

