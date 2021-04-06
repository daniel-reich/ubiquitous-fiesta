
def is_anagram(s1, s2):
  s1sort = sorted(s1.lower())
  s2sort = sorted(s2.lower())
  if s1sort == s2sort:
    return True
  else:
    return False

