
def nearest_vowel(s):
  l='aeiou'
  d=[abs(ord(s)-ord(i)) for i in l]
  return l[d.index(min(d))]

