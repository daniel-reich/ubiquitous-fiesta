
def is_anagram(s1, s2):
  s1 = s1.lower()
  s2 = s2.lower()
  for eachletter in s2:
    x = s1.count(eachletter)
    y = s2.count(eachletter)
    if x == y:
      continue
    else:
      return False
  return True

