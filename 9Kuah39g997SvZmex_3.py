
def common_last_vowel(txt):
  v = 'aeiou'
  for i in txt.lower()[::-1]:
    if i in v:
      return i

