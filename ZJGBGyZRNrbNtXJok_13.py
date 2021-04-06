
def nearest_vowel(s):
  vowel = "aeiou"
  a = [abs(ord(s)-ord(i)) for i in vowel]
  return vowel[a.index(min(a))]

