
def nearest_vowel(s):
  return min('aeiou', key=lambda x:abs(ord(x)-ord(s)))

