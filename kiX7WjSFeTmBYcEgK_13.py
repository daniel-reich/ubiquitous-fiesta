
def major_sum(lst):
  p, n, z = 0, 0, 0
​
  for l in lst:
    if l == 0:
      z += 1
    elif l > 0:
      p += l
    elif l < 0:
      n += l
  if max(z, p, -n) == z:
    return z
  elif max(z, p, -n) == p:
    return p
  elif max(z, p, -n) == -n:
    return n

