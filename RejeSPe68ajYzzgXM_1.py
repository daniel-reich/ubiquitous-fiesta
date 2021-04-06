
def combine(lst):
  sub = lambda s: sorted([k for k in lst if k[0] == s])
  return {k[0]: [m[2] for m in sub(k[0])] for k in lst}

