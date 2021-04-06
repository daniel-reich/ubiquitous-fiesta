
def nearest_vowel(s):
  return min('aeiou', key=lambda v: abs(ord(s)-ord(v)))

