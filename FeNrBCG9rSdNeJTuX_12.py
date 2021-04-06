
def max_possible(n1, n2):
  digs = [int(i) for i in str(n1)]
  digs2 = [int(i) for i in str(n2)]
  for n in range(len(digs)):
    if len(digs2)>0:
      m = max(digs2)
      if m > digs[n]:
        digs[n] = m
        digs2.remove(m)
  s = ''
  for dig in digs:
    s += str(dig)
  return int(s)

