
def is_undulating(n):
  s = str(n)
  if len(s) < 3:
    return False
  if len(set(s)) != 2:
    return False
  a = s[0]
  for i in s[1:]:
    if a == i:
      return False
    a = i
  return True

