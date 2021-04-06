
def lengthen(s1, s2):
  if len(s1) > len(s2):
    a = s2
    b = s1
  else:
    a = s1
    b = s2
  sol = a
  while len(sol) < len(b):
    sol += a
  return sol[:len(b)]

