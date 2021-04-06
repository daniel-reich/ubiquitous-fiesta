
def can_build(s1, s2):
  return True if s2 == "" else len(''.join(x for x in s2 if x in s1 and s1.count(x) >= s2.count(x))) >= len(s2)

