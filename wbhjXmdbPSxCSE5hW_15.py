
def sigilize(desire):
  x = ''.join(desire.upper().split())
  for v in 'AEIOU':
    x = x.replace(v, '')
  for c in x:
    if x.count(c) > 1:
      x = x[:x.index(c)] + x[x.index(c)+1:]
  return x

