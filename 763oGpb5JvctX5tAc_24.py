
def is_anagram(s1, s2):
  return sorted([c.lower() for c in s1]) == sorted([c.lower() for c in s2])

