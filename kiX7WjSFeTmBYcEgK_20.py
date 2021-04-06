
def major_sum(l):
  p = 0
  n = 0
  z = 0
  for i in l:
    if i < 0: n += i
    if i > 0: p +=i
    if i == 0: z += 1
  if abs(n) > p and abs(n) > z: return n
  if p > abs(n) and p > z: return p
  if z > abs(n) and z > p: return z

