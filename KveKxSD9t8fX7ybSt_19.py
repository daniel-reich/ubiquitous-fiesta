
def final_countdown(r):
  c, t = list(), list()
  for i, n in enumerate(r[::-1]):
    if t:
      if n == 1: c, t = c+[t[::-1]], [n]
      elif n-t[-1] == 1: t += [n]
      else: c, t = c+[t[::-1]], []
    elif n == 1: t +=[n]
    if i+1 == len(r) and t: c += [t[::-1]]
  return [len(c), c[::-1]]

