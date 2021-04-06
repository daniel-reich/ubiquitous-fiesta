
def is_anagram(s1, s2):
  return sum([ord(x) for x in s1.lower()]) == sum([ord(x) for x in s2.lower()])

