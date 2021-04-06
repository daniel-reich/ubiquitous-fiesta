
def is_zygodrome(num):
  n = str(num)
  pair = lambda x: len(x) > 1 and all(i == x[0] for i in x)
  n = ''.join([n[i] + ' ' if n[i] != n[i+1] else n[i] for i in range(len(n)-1)] + [n[-1]])
  return all(pair(i) for i in n.split())

