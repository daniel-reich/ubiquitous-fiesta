
def can_build(s1, s2):
  for c in s1:
    s2 = s2.replace(c, "", 1)
  return s2 == ""

