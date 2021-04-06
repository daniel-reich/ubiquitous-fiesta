
def is_undulating(n):
  if len(str(n)) < 3: return False
  if len(set(str(n))) != 2: return False
  s = str(n)
  for i in range(len(s)-1):
    if s[i] == s[i+1]: return False
  return True

