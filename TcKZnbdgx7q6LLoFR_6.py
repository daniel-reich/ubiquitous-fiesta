
def collect(s, n, l = [], i = 0, ni = 0, st = ''):
  if i == 0:
    l = []
  if i == len(s):
    if len(st) == n:
      l.append(st)
    return sorted(l)
  else:
    if ni == n:
      l.append(st)
      ni = 0
      st = ''
    st += s[i]
    ni += 1
    i += 1
    
    return collect(s, n, l, i, ni, st)
  # your recursive solution here

