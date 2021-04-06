
def can_pay_cost(m, c):
  n = int(''.join(x for x in c if x.isdigit()) or '0')
  M, C = {x: m.count(x) for x in m}, \
         {x: c.count(x) for x in set(c) if x.isalpha()}
  M = {x: y-C[x] if x in C.keys() else y for x, y in M.items()}
  return all(x > -1 for x in M.values()) and -1 < -n+sum(M.values()) \
     and all(x in M.keys() for x in C.keys())

