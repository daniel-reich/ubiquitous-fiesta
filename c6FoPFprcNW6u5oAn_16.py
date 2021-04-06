
def farey(s):
  gcd, f = lambda a, b: gcd(b, a % b) if b else a, []
  for d in range(s, 1, -1):
    for n in range(1, d):
      if gcd(n, d) == 1: f += ['{}/{}'.format(n, d)]
  return sorted(['0/1']+f+['1/1'], key=lambda x: eval(x))

