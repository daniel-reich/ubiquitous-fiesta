
def bit_rotate(n, m, d):
  aux = n
  r = []
  while aux > 0:
    r.append(str(aux&1))
    aux //= 2
  r = r if len(r) > 0 else ['0']
  r = ''.join(r[::-1])
  for i in range(m):
    if d:
      r = r[-1] + r[:-1]
    else:
      r = r[1:] + r[0]
  return sum([int(r[i])*(2**(len(r)-i-1)) for i in range(len(r))])

