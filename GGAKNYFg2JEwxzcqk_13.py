
def anti_divisors(n): #w/o built-in
  s, a_d = 1, []
  while s < n:
    if n % s:
      if s % 2:
        if not (n * 2 - 1) % s or not (n * 2 + 1) % s:
          a_d += [s]
      else:
        if not (n * 2) % s:
          a_d += [s]
    s += 1
  return a_d

