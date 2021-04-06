
def can_build(s1, s2):
  if s2 and s2[0] in s1:
    return can_build(s1.replace(s2[0], "", 1), s2[1:])
  return not bool(s2)

