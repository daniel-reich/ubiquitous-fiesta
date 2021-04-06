
def flatten(r):
  def f(l):
      for x in iter(l):
          if isinstance(x,list):yield from f(x)
          else:yield x
  return list(f(r))

