
def junction_or_self(n):
  e = []
  def su(nu): 
    c = nu
    h = list(str(nu))
    for a in range(len(h)):
      h[a] = int(h[a])
    for b in h:
      c = b + c
    return c
  for a in range(1,n):
    if su(a) == n:
      e.append(a)
  e.reverse()
  return e if e != [] else 'Self'

