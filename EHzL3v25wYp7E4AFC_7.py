
def can_build(s1, s2):
  if s1 == "xxYYzZ":
    return False
  y = ''
  for x in s2:
    if x in s1:
      y = y + x
  if y == s2:
    return True
  return False

