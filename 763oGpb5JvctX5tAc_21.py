
def is_anagram(s1, s2):
  s1 = list(str.lower(s1))
  s2 = list(str.lower(s2))
  list.sort(s1) 
  list.sort(s2)
  return s1 == s2

