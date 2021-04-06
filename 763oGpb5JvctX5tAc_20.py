
def is_anagram(s1, s2):
  lower_s1 = s1.lower()
  lower_s2 = s2.lower()
  lower_s1_sorted = ''.join(sorted(lower_s1))
  lower_s2_sorted = ''.join(sorted(lower_s2))
  if lower_s1_sorted == lower_s2_sorted:
    return True
  else:
    return False

