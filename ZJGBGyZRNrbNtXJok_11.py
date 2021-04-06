
def nearest_vowel(s):
  vowels = 'aeiou'
  a = 'abcdefghijklmnopqrstuvwxyz'
  if s in vowels:
    return s
  for i in range(1,6):
    if a.index(s)-i>=0 and a.index(s)+i<len(a):
      if a[a.index(s)-i] in vowels and a[a.index(s)+i] in vowels:
        return a[a.index(s)-i]
    if a.index(s)-i>=0 and a[a.index(s)-i] in vowels:
      return a[a.index(s)-i]
    if a.index(s)+i<len(a) and a[a.index(s)+i] in vowels:
      return a[a.index(s)+i]

