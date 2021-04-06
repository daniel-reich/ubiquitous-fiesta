
def flatten(r):
  if r == []:
    return r
  if isinstance(r[0], list):
    return flatten(r[0]) + flatten(r[1:])
  return r[:1] + flatten(r[1:])

