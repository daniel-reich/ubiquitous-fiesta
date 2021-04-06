
def widen_streets(lst, n):
  def widen():
    for s in (''.join(r) for r in zip(*lst)):
      for _ in range(1 if s.strip() else n): yield s
      
  return [''.join(r) for r in zip(*widen())]

