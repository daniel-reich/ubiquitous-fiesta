
def make_sandwich(i, f):
  b = []
  for a in i:
    if a == f:
      b.append("bread")
      b.append(f)
      b.append("bread")
    else:
      b.append(a)
  return b

