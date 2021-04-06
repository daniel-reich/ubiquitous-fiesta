
def grant_the_hint(txt):
  a = []
  m = txt.split()
  n = len(max(m, key=len))
  for x in m:
    l = len(x)
    a.append([x[:i] + (l - i) * '_'  for i in range(n+1)])
  return list(map(lambda x: ' '.join(x), zip(*a)))

