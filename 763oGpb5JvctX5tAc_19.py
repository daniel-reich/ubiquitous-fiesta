
def is_anagram(s1,s2):
  return ''.join(sorted(s1.lower())) == ''.join(sorted(s2.lower()))

