
def nearest_vowel(s):
  v = 'aeiou'
  return sorted([(abs(ord(s) - ord(x)), x) for x in v])[0][1]

