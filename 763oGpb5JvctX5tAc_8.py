
def is_anagram(s1, s2):
  s1 = s1.lower()
  s2 = s2.lower()
  l1 = [s1[i] for i in range(len(s1))]
  l2 = [s2[i] for i in range(len(s2))]
  return sorted(l1) == sorted(l2)

