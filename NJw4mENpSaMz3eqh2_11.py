
def is_undulating(n):
  s = list(str(n))
  if len(s) < 3 or len(set(s)) != 2: return False
  return all(a!=b for a,b in zip(s, s[1:]))

