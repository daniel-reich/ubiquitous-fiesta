
def is_economical(n):
  def primes(n):
    factors, current, do = [n], [0,2], True
    while do:
      if current[1] >= factors[0]:
        do = False
      elif not factors[0] % current[1]:
        current[0] += 1
        factors.append([0,current[1]])
        while not factors[0] % current[1]:
          factors[0] /= current[1]
          factors[current[0]][0] += 1
      current[1] += 1
    if factors[0] != 1.0: factors.append([1,int(factors[0])])
    return factors[1:]
  pf = primes(n)
  digs = lambda a: len(str(a))
  digpf = sum([digs(pf[i][0])+digs(pf[i][1]) if pf[i][0] != 1 else digs(pf[i][1]) for i in range(len(pf))])
  if digs(n) == digpf: return "Equidigital"
  elif digs(n) > digpf: return "Frugal"
  else: return "Wasteful"

