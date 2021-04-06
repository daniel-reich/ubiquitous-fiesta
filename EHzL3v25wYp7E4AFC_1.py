
def can_build(s1, s2):
  return all(s2.count(i) <= s1.count(i) for i in s2)

