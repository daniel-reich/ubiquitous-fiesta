
def nearest_vowel(s):
  return min('aeiou', key=lambda x: abs(ord(s) - ord(x)))

