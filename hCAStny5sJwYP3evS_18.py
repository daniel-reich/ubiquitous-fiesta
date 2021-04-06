
def is_early_bird(_range, n):
  s = ''
  t = []
  for i in range(_range + 1):
    if i == n:
      for j in range(len(str(i))):
        t.append(len(s) + j)
    s += str(i)
  u, sn = [], str(n)
  for i in range(len(s) - len(str(n)) + 1):
    if s[i:i + len(str(n))] == sn:
      u.append([k for k in range(i, i + len(str(n)))])
  if t != u[0]:
    return u + ['Early Bird!']
  return u

