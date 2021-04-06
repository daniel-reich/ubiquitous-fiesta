
def is_anagram(s1, s2):
  upper1 = s1.upper()
  upper2 = s2.upper()
  ordre1 = sorted(upper1)
  ordre2 = sorted(upper2)
  if ordre1 == ordre2:
    return True
  else:
    return False

