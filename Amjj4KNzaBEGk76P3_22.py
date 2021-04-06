
def chemical_reactions(carbon, hydrogen, oxygen):
  res = []
  h,o = 0,0
  while h + 2 <= hydrogen and o+1 <= oxygen:
    h += 2
    o += 1
  hydrogen -= h
  oxygen -= o
  res.append(o)
  c,o = 0,0
  while c+1 <= carbon and o+2 <= oxygen:
    c += 1
    o += 2
  carbon -= c
  oxygen -= o
  res.append(c)
  c,h = 0,0
  while c + 1 <= carbon and h+4 <= hydrogen:
    c += 1
    h += 4
  res.append(c)
  return res

