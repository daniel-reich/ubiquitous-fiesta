
def num_type(n):
  s = []
  for i in range(1,n):
    if n%i == 0:
      s.append(i)
  if sum(s) == n:
    return "Perfect"
  v = sum(s)
  l = []
  for i in range(1,v):
    if v%i == 0:
      l.append(i)
  if sum(l) == n:
    return "Amicable"
  return "Neither"

