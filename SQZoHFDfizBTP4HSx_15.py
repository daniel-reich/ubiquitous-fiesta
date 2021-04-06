
def missing_alphabets(n):
  c = {}
  for x in n:
    if c.get(x) == None:
      c[x] = 0
    c[x] += 1
  t = sorted(c.values())[-1]
  out = "".join([a*t for a in 'abcdefghijklmnopqrstuvwxyz'])
  for x in n:
    out = out.replace(x, '', 1)
  return out

