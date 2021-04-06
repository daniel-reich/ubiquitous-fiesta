
def josephus(n):
  if n==0:
    return False
  def jos(k,P):
    if len(P) == 1:
      return P[0]
    P.remove(P[(k+1) % len(P)])
    return jos((k+1) % (len(P)+1), P)
  return jos(0, [i for i in range(n)])

