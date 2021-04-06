
def is_autobiographical(n):
  if n < 1 or n >= 10**10:
    return False
  
  s = str(n)
  return all(s.count(str(i)) == int(ch) for i, ch in enumerate(s))

