
def flatten(r):
  out = []
  for i in r:
    if type(i) is list:
      for j in flatten(i):
        out.append(j)
    else:
      out.append(i)
  return out

