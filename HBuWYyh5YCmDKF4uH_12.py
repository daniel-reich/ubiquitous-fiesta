
def almost_sorted(r):
  s = sorted(r[:])
  if r == s or r == s[::-1]: return False
  for i in range(len(r)):
    a = [n for k, n in enumerate(r) if k != i]
    if a in [sorted(a), sorted(a)[::-1]]: return True
  return False

