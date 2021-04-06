
def mod_inv(n, m):
  s1, s0 = 0, 1
  t1, t0 = 1, 0
  r1, r0 = m, n
  while r1:
    q = r0 // r1
    r0, r1 = r1, r0 - q * r1
    s0, s1 = s1, s0 - q * s1
    t0, t1 = t1, t0 - q * t1
  if s0 < 0: s0 += m
  return s0 if r0 == 1 else False

