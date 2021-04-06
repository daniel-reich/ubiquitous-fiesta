
def score_it(k, s=0, x=0, y=0, i=0):
  if i >= len(k): return s
  if k[i] == '(': x, i = x + 1, i + 1
  elif k[i] == ')': y, i = y + 1, i + 1
  elif k[i] in '0123456789':
    n = str()
    while k[i] in '0123456789': n, i = n + k[i], i + 1
    s += int(n) * (x - y)
  else: i += 1
  return score_it(k, s, x, y, i)

