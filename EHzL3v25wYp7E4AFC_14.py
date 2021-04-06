
def can_build(s1, s2):
  return all([s2.count(letter) <= s1.count(letter) for letter in s2]);

