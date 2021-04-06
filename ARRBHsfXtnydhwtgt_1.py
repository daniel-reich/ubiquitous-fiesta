
def compress(c, s=None):
  if s is None: return compress(c[1:], [c[0]])
  if not len(c):
    return ''.join(x[0] + ['', str(len(x))][len(x) > 1] for x in s)
  if c[0] in s[-1]:
    while len(c) and c[0] in s[-1]: c, s[-1] = c[1:], s[-1] + c[0]
  else: c, s = c[1:], s + [c[0]]
  return compress(c, s)

