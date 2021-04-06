
next_rand = lambda a, x: (a*x + 1)%65535
​
def random(lst):
  r1, r2 = lst
  if r1 == r2: return r1
  a = None
  for y in range(65535):
    av = (r2 - 1 + 65535 * y) / r1
    if av%1 == 0:
      if not a:
        a = int(av)
      elif av > 65535:
        break
      else:
        return None
    y += 1
  return next_rand(a, r2)

