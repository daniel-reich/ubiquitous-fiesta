
def mumbling(s):
  u = s.upper()
  l = s.lower()
  return '-'.join('{}{}'.format(u[i], l[i] * i) for i in range(len(s)))

